#!usr/bin/python
import random
import string

def pickrandomchar():
	chance = random.randint(1,100)

	if chance <=20:

		x= random.randint(0,9)
		return x
	if chance >=21:
		x= random.choice(string.letters)
		return x

def genpassword(length):
	password = []

	for a in range(0,length):
		password.append(str(pickrandomchar()))

	passstring = "".join(password)
	return passstring

print(genpassword(8))