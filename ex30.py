#!/usr/bin/python3
import random

with open('sowpods.txt', 'r') as open_file:
	line = open_file.readline()
	wordlist = []
	while line:
		wordlist.append(line.strip())
		line = open_file.readline()

secure_random = random.SystemRandom() #not needed but this is how to do cryptographically secure random.
print(secure_random.choice(wordlist))