#!/usr/bin/python3
#using json file as a database for names / birthdays.

import json
import re
from collections import Counter

def addnewentry(mydict):
	name = input("\nType name for new entry. ")
	while True:
		birthday = input("Type birthday of new entry. ")
		if verifydateformat(birthday) == True:
			mydict.update({name: birthday})
			return mydict
		else:
			print("Birthday in incorrect format. Please use dd/mm/yyyy.\n")

def verifydateformat(mystring):
	dateformat = re.compile(r'\b\d\d/\d\d/\d\d\d\d\b')
	match = dateformat.findall(mystring)
	if match:
		return True
	else:
		return False

def writetojson(mydict,target):
	with open(target, "w") as f:
		json.dump(mydict, f)

def removeentry(mydict):
	name = input("\nType name to delete from database. ")
	if name in mydict:
		del mydict[name]
	return mydict

def printallkeys(mydict):
	
	print(mydict.keys())
	print("\n")

def countindict(mydict):
	monthlist =[]
	yearlist =[]

	monthdict = { "01" : "Jan", "02" : "Feb", "03" : "Mar",
	"04" : "April", "05" : "May", "06": "Jun",
	"07" : "Jul", "08": "Aug", "09" : "Sep",
	"10" : "Oct", "11" : "Nov", "12" : "Dec"}

	for key in mydict:
		monthlist.append(monthdict[mydict[key][3:5]])
		yearlist.append(mydict[key][6:10])

	monthcount = Counter(monthlist)
	yearcount = Counter(yearlist)
	print("\nCount of birthdays by month")
	print(monthcount)
	print("\nCount of birthdays by year")
	print(yearcount)
		
	pass

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
print("\nThis dict based database stores people's name and corresponding birthday.\nYou may search the database, add or delete entries.\n")

while True:
	nextaction = input("What do you want to do? (Add, Remove, Find, Count, List, Quit) \n").capitalize().strip()

	if nextaction == "Add":
		info = addnewentry(info)
		writetojson(info, filename)

	if nextaction == "Remove":
		info = removeentry(info)
		writetojson(info, filename)

	if nextaction == "Find":
		findbirthdaybyname(info)

	if nextaction == "Count":
		countindict(info)

	if nextaction == "List":
		printallkeys(info)

	if nextaction == "Quit":
		print('Good Bye')
		raise SystemExit(0)


