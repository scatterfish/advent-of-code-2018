#!/usr/bin/env python

import os
import sys

def main():
	print("Hello, world!")

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("\nKeyboard interrupt received. Exiting...")
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)

