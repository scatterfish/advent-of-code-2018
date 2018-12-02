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

def exitwitherror(message):
	print("Error! %s\nExiting..." % message, file=sys.stderr)
	sys.exit(1)

def getyesno(prompt):
	print(prompt)
	while True:
		response = input("(Y/N): ").lower()
		if response == "y" or response == "yes":
			return True
		elif response == "n" or response == "no":
			return False
		else:
			print("Please enter a valid input (Y/N/Yes/No)")

def getint(prompt):
	print(prompt)
	while True:
		try:
			response = int(input(">>>"))
			return response
		except KeyboardInterrupt:
			print("\nKeyboard interrupt received. Exiting...")
		except ValueError:
			print("Please enter a valid integer.")
		except:
			exitwitherror("Failed to read integer input")

def checkdir(name):
	dirpath = path(name)
	if not dirpath.exists():
		print("\"%s\" directory not found. Making a new one..." % name)
		try:
			dirpath.mkdir()
			return True # directory created
		except:
			exitwitherror("Failed to create directory \"%s\"" % name)
	elif dirpath.is_file():
		exitwitherror("Cannot create \"%s\" directory because it is a file" % name)
	return False # directory found



def populatetemplates():
	print("Created new templates directory, please check howto.txt")
	path("templates/howto.txt").write_text((
		"This is the directory containing project templates for various languages.\n"
		"Each template is a directory, and in that directory are all of the files and folders for the template that will be copied when making a new project.\n"
		"Templates for C, Python, and Rust are included. Feel free to use them as exmaples and/or modify them!\n"
		"The only reserved template name is \"blank\". A custom template named \"blank\" will simply be ignored.\n"
	))
	path("templates/c").mkdir()
	path("templates/c/out").mkdir()
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
		"#!/bin/python\n"
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
	path("templates/rust/src/main.rs").write_text((
		"fn main() {\n"
		"	println!(\"Hello, world!\");\n"
		"}\n"
	))
	sys.exit(0)

def main():
	
	# ensure that all of the directories exist
	checkdir("puzzles")
	if checkdir("templates"):
		populatetemplates()
	
	# get the paths for the templates and existing puzzle projects
	templates = [t for t in path("templates").glob("*") if t.is_dir()]
	puzzles = [e for e in path("puzzles").glob("*") if e.is_dir()]
	
	# get the day numbers for the existing puzzle projects
	days = []
	for e in puzzles:
		try:
			d = int(e.name[0:2])
			days.append(d)
		except:
			exitwitherror("Failed to parse day number for \"%s\"" % e.name)
	
	# determine the highest day number so far
	maxday = 0
	for d in days:
		if d <= 0:
			exitwitherror("Got invalid day number for \"%s\"" % e.name)
		if d > maxday:
			maxday = d
	day = maxday + 1
	
	print((
		"---------------------------------------------------\n"
		"Welcome to the Advent of Code puzzle project maker!\n"
		"---------------------------------------------------"
	))
	
	# get the day of the puzzle
	daycorrect = getyesno("It seems that it's day %d. Is this correct?" % day)
	if not daycorrect:
		while True:
			day = getint("Please enter the current day.")
			if day in days:
				if getyesno("There already exists a project for day %d. Are you sure?" % day):
					break;
			else:
				break;
	
	# get string for the day number
	daystr = ""
	if day < 10:
		daystr = "0" + str(day)
	else:
		daystr = str(day)
	
	# get puzzle name and format it
	puzzlename = ""
	template = ""
	while True:
		print("Please enter the puzzle name. (e.g. Inverse Captcha)")
		puzzlename = input(">>>").lower()
		puzzlename = re.sub(r"[\/\\\?\%\*\:\|\"\<\>\.\,\!\@\#\$\^\&\;\-\_\+\=\`\~]", " ", puzzlename)
		puzzlename = re.sub(r" +", "-", puzzlename)
		puzzlename = puzzlename.strip()
		choices = ["blank"]
		for t in templates:
			choices.append(t.name)
		choicesstr = ""
		for i in range(0, len(choices)):
			choicesstr += choices[i]
			if not i == len(choices) - 1:
				choicesstr += ", "
		print("Please select a template to use.")
		print("The available choices are: " + choicesstr)
		while True:
			template = input(">>>")
			if template in choices:
				break
			else:
				print("Please enter a valid template name.")
		puzzlename = "%s-%s-%s" % (daystr, puzzlename, template.upper())
		print("The directory \"%s\" will be created." % puzzlename)
		if getyesno("Is this correct?"):
			break
	
	dst = path("puzzles/%s" % puzzlename)
	if not template == "blank":
		src = path("templates/%s" % template)
		dst = path("puzzles/%s" % puzzlename)
		try:
			shutil.copytree(src, dst)
		except:
			exitwitherror("Failed to copy \"%s\" template tree to \"%s\"" % (template, puzzlename))
		print("Done! Created directory \"%s\" with the \"%s\" template." % (puzzlename, template))
	else:
		try:
			dst.mkdir()
		except:
			exitwitherror("Failed to create directory \"%s\"" % puzzlename)
		print("Done! Created directory \"%s\"" % puzzlename)

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("\nKeyboard interrupt received. Exiting...")
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)
