#!/bin/python3

# Amy's Advent of Code project maker
# @Tyrov on GitHub
# Scatterfish#8418 on Discord

import os
import sys
import stat
import re
import shutil
from pathlib import Path as path

def exit_with_error(message):
	print("Error! %s\nExiting..." % message, file=sys.stderr)
	sys.exit(1)

def get_yes_no(prompt):
	print(prompt)
	while True:
		response = input("(Y/N): ").lower()
		if response == "y" or response == "yes":
			return True
		elif response == "n" or response == "no":
			return False
		else:
			print("Please enter a valid input (Y/N/Yes/No)")

def get_day(prompt):
	print(prompt)
	while True:
		try:
			response = input(">>>")
			if not response == "":
				response = int(response)
				if response > 0:
					return response
				else:
					print("Please enter a valid day number.")
			else:
				return 0
		except KeyboardInterrupt:
			print("\nKeyboard interrupt received. Exiting...")
		except ValueError:
			print("Please enter a valid integer.")
		except:
			exit_with_error("Failed to read integer input")

def check_dir_exists(name):
	dir_path = path(name)
	if not dir_path.exists():
		print("\"%s\" directory not found. Making a new one..." % name)
		try:
			dir_path.mkdir()
			return True # directory created
		except:
			exit_with_error("Failed to create directory \"%s\"" % name)
	elif dir_path.is_file():
		exit_with_error("Cannot create \"%s\" directory because it is a file" % name)
	return False # directory found

def populate_templates():
	print("Created new templates directory, please check howto.txt")
	path("templates/howto.txt").write_text((
		"This is the directory containing project templates for various languages.\n"
		"Each template is a directory, and in that directory are all of the files and folders for the template that will be copied when making a new project.\n"
		"Templates for C, Python, and Rust are included. Feel free to use them as exmaples and/or modify them!\n"
		"The only reserved template name is \"blank\". A custom template named \"blank\" will simply be ignored.\n"
	))
	path("templates/c").mkdir()
	path("templates/c/out").mkdir()
	path("templates/c/out/.keep").write_text("")
	path("templates/c/input.txt").write_text("")
	path("templates/c/main.c").write_text((
		"#include <stdio.h>\n"
		"#include <stdlib.h>\n"
		"\n"
		"int main() {\n"
		"	printf(\"Hello, world!\\n\");\n"
		"	return 0;\n"
		"}\n"
	))
	p = path("templates/c/build.sh")
	p.write_text((
		"#!/bin/sh\n"
		"\n"
		"gcc main.c -o out/main\n"
		"exec out/main\n"
	))
	p.chmod(p.stat().st_mode | stat.S_IEXEC)
	path("templates/python").mkdir()
	path("templates/python/input.txt").write_text("")
	p = path("templates/python/main.py")
	p.write_text((
		"#!/usr/bin/env python3\n"
		"\n"
		"def main():\n"
		"	print(\"Hello, world!\")\n"
		"\n"
		"if __name__ == \"__main__\":\n"
		"	main()\n"
	))
	p.chmod(p.stat().st_mode | stat.S_IEXEC)
	path("templates/rust").mkdir()
	path("templates/rust/src").mkdir()
	path("templates/rust/src/input.txt").write_text("")
	path("templates/rust/Cargo.toml").write_text((
		"[package]\n"
		"name = \"rust\"\n"
		"version = \"0.1.0\"\n"
		"authors = [\"\"]\n"
		"\n"
		"[dependencies]\n"
	))
	path("templates/rust/.gitignore").write_text((
		"target/\n"
		"Cargo.lock\n"
	))
	path("templates/rust/src/main.rs").write_text((
		"fn main() {\n"
		"	println!(\"Hello, world!\");\n"
		"}\n"
	))
	sys.exit(0)

def main():
	
	# ensure that all of the directories exist
	check_dir_exists("solutions")
	if check_dir_exists("templates"):
		populate_templates()
	
	# get the paths for the templates and existing solution projects
	templates = [t for t in path("templates").glob("*") if t.is_dir()]
	solutions = [e for e in path("solutions").glob("*") if e.is_dir()]
	
	# get the day numbers for the existing solution projects
	days = []
	for e in solutions:
		try:
			d = int(e.name[0:2])
			days.append(d)
		except:
			exit_with_error("Failed to parse day number for \"%s\"" % e.name)
	
	# determine the highest day number so far
	max_day = 0
	for d in days:
		if d <= 0:
			exit_with_error("Got invalid day number for \"%s\"" % e.name)
		if d > max_day:
			max_day = d
	day = max_day + 1
	
	print((
		"---------------------------------------------------\n"
		"Welcome to the Advent of Code solution project maker!\n"
		"---------------------------------------------------"
	))
	
	# get the day of the puzzle
	day_to_use = get_day("Please enter the day for the puzzle. (Default: %d)" % day)
	if not day_to_use == 0:
		day = day_to_use
	
	# get string for the day number
	day_str = ""
	if day < 10:
		day_str = "0" + str(day)
	else:
		day_str = str(day)
	
	# get solution name and format it
	solution_name = ""
	template = ""
	while True:
		print("Please enter the puzzle name. (e.g. Inverse Captcha)")
		solution_name = input(">>>").lower()
		solution_name = re.sub(r"[\/\\\?\%\*\:\|\"\<\>\.\,\!\@\#\$\^\&\;\-\_\+\=\`\~]", " ", solution_name)
		solution_name = re.sub(r" +", "-", solution_name)
		solution_name = solution_name.strip()
		choices = ["blank"]
		for t in templates:
			choices.append(t.name)
		choices_str = ""
		for i in range(0, len(choices)):
			choices_str += choices[i]
			if not i == len(choices) - 1:
				choices_str += ", "
		print("Please select a template to use.")
		print("The available choices are: " + choices_str)
		while True:
			template = input(">>>")
			if template in choices:
				break
			else:
				print("Please enter a valid template name.")
		solution_name = "%s-%s-%s" % (day_str, solution_name, template.upper())
		print("The directory \"%s\" will be created." % solution_name)
		if get_yes_no("Is this correct?"):
			break
	
	dst = path("solutions/%s" % solution_name)
	if not template == "blank":
		src = path("templates/%s" % template)
		dst = path("solutions/%s" % solution_name)
		try:
			shutil.copytree(src, dst)
		except:
			exit_with_error("Failed to copy \"%s\" template tree to \"%s\"" % (template, solution_name))
		print("Done! Created directory \"%s\" with the \"%s\" template." % (solution_name, template))
	else:
		try:
			dst.mkdir()
		except:
			exit_with_error("Failed to create directory \"%s\"" % solution_name)
		print("Done! Created directory \"%s\"" % solution_name)

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("\nKeyboard interrupt received. Exiting...")
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)
