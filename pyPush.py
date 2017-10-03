'''
A quick script I wrote up to help me better drill in the art of win32 shellcoding
returns the push opcodes to place strings on the stacks
'''

import re
import sys


def reverseInput(text):
	#Reverses the input
	text = text[::-1]
	return text


def toHex(char):
	#Hard one to figure out, Takes input and returns ASCII :)
	return str(char).encode("hex")


def formatItem(value):
	#Not really needed, just to make it more understandable
	#Returns the value in hex format
	return b"\\x{}".format(value)


def main():

	start = sys.argv[1]
	hexedlist = []
	Shellcode = []
	print "[*] Converting [", start, "] to PUSH instructions" + "\n"

	for char in reverseInput(start):
		hexedlist.append(toHex(char))

	for item in hexedlist:
		Shellcode.append(formatItem(item))

	Shellcode.insert(3, "\\x00")

	for item in re.findall('.'*16, ''.join(Shellcode)):
		print "\\x68" + ''.join(item)


if "__main__" == __name__:
	if sys.argv[:] < 2:
		print "USAGE python pyPush.py (STRING TO CONVERT)"

	else:
		print "****************"
		print "String to PUSH instructions"
		print "****************" + "\n"
		main()

