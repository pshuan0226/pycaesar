#!/usr/bin/python

import string
import argparse
import sys

def encoder(plaintext, shift):
	alphabet = string.ascii_lowercase
	shifted_alphabet = alphabet[int(shift):] + alphabet[:int(shift)]
	# print shifted_alphabet
	table = string.maketrans(alphabet, shifted_alphabet)
	print(plaintext.translate(table))

def decoder(plaintext, shift):
	if shift != 0:
		alphabet = string.ascii_lowercase
		current_alphabet = alphabet[int(shift):] + alphabet[:int(shift)]
		table = string.maketrans(current_alphabet, alphabet)
		print(plaintext.translate(table))
	#enumerate all possible up to 25 shifts
	else:
		for sh in range(1, 26):
			alphabet = string.ascii_lowercase
			current_alphabet = alphabet[int(sh):] + alphabet[:int(sh)]
			table = string.maketrans(current_alphabet, alphabet)
			print(plaintext.translate(table))


def usage():
	print('Format: pycaesar [text] [shift] [mode: d/e]')
	print('d: decode the cipher')
	print('e: encode the plaintext with caesar cipher')
	return

def main():
	parser = argparse.ArgumentParser(description='pycaesar: ceasar cipher in python')
	parser.add_argument("text", help='text you would like to decode/encode')
	parser.add_argument("-s", "--shift", type=int, help='number of shifts (don\'t specify if unknown)', default=0)
	parser.add_argument("-e", "--encode", help="encodes with ceasar cipher", action='store_true')
	parser.add_argument("-d", "--decode", help="decodes the cipher", action='store_true')

	# parse input arguments
	args = parser.parse_args()
	shift = args.shift
	text = args.text

	if args.encode:
		encoder(text, shift)
	elif args.decode:
		decoder(text, shift)

if __name__ == '__main__':
	main()
