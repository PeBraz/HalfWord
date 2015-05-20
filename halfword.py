#!/usr/bin/env python

import re

##
##	Allows writing a phrase using only half the characters needed
##	If using a application where, every character is unicode and there is a limit. 
##  Encoding using enc() function allows to transform an 8-bit phrase into a 16-bit phrase 
##	using only half the characters. You can write more with less. ;D
##

def enc(string):
	"""
		Encodes two 8-bit character into a 16-bit unicode character
	"""
	unif = lambda a ,b : unichr(int("{}{}".format(a,b, '02'), base=16))
	char_to_hex = lambda a : hex(ord(a)).split('x')[1]

	chars = list(string)
	s = ''
	for (a,b) in zip(chars[::2], chars[1::2]): #eats last char if length odd
		s += unif(char_to_hex(a),char_to_hex(b))
	if len(chars) % 2 == 1:
		s += unif(char_to_hex(chars[-1]),'00')
	return s

def dec(string):
	"""
		Decodes a 16 bit unicode character into two 8-bit characters
	"""
	hex_to_char = lambda h: chr(int(('0x'+h), base=16))

	s = ""
	for unic in string:
		hx_str = re.sub('[^0-9a-f]', '', repr(unic))
		s += hex_to_char(hx_str[:2]) +\
				(hex_to_char(hx_str[2:]) if hx_str[2:] else '')
	return s

