#!/usr/bin/python

import string
import getopt
import sys

def encoder(plaintext, shift):
	alphabet = string.ascii_lowercase
	shifted_alphabet = alphabet[int(shift):] + alphabet[:int(shift)]
	# print shifted_alphabet
	table = string.maketrans(alphabet, shifted_alphabet)
	print(plaintext.translate(table))

def decoder(plaintext, shift):
	alphabet = string.ascii_lowercase
	current_alphabet = alphabet[int(shift):] + alphabet[:int(shift)]
	table = string.maketrans(current_alphabet, alphabet)
	print(plaintext.translate(table))

def usage():
	print('Format: pycaesar [text] [shift] [mode: d/e]')
	print('d: decode the cipher')
	print('e: encode the plaintext with caesar cipher')
	return

def main():
	try:
		if len(sys.argv) < 4:
			usage()
			sys.exit(1)
		opts, args = getopt.getopt(
			sys.argv[3:], "hde", ["help", "decode", "encode",])
	except getopt.GetoptError as err:
		# print help information and exit:
		# will print something like "option -a not recognized"
		print str(err) 
		usage()
		sys.exit(2)

	mode = None
	for o, a in opts:
		if o in ("-e", "--encode"):
			mode = 'e'
		elif o in ("-d", "--decode"):
			mode = 'd'
		elif o in ("-h", "--help"):
			usage()
			sys.exit()
		else:
			assert False, "unhandled option"

	text = sys.argv[1]
	shift = sys.argv[2]
	if mode == 'e':
		encoder(text, shift)
	else:
		decoder(text, shift)

if __name__ == '__main__':
	main()
