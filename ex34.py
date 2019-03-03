#!/usr/bin/python3
#using json file as a database for names / birthdays.

import json

def addnewentry(mydict):
	name = input("Type name for new entry. ")
	birthday = input("Type birthday of new entry. ")
	mydict.update({name: birthday})
	return mydict

def writetojson(mydict,target):
	with open(target, "w") as f:
		json.dump(mydict, f)

def removeentry(mydict):
	name = input("Type name to delete from database. ")
	if name in mydict:
		del mydict[name]
	return mydict

def printallkeys(mydict):
	print(mydict.keys())

def loadjson(target):
	with open(target, "r") as f:
	    mydict = json.load(f)
	    return mydict

def findbirthdaybyname(mydict):
	print("Please enter a name and the program will output their corresponding birthday")
	choice = input()
	print("{}'s birthday is on {}".format(choice, mydict.get(choice, "No person of that name within the database.")))

filename = "bdays.json"
info = loadjson(filename)
printallkeys(info)
print("This dict based database stores people's name and corresponding birthday.\n You may search the database, add or delete entries.\n")

while True:
	nextaction = input("What do you want to do? (Add, Remove, Find, Quit) ").capitalize().strip()

	if nextaction == "Add":
		info = addnewentry(info)
		writetojson(info, filename)

	if nextaction == "Remove":
		info = removeentry(info)
		writetojson(info, filename)

	if nextaction == "Find":
		findbirthdaybyname(info)

	if nextaction == "Quit":
		print('Good Bye')
		raise SystemExit(0)

