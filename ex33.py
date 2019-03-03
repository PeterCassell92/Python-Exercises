#!/usr/bin/python3

bdaydict = {
		"Ashleigh Cooper": "27/06/1992",
		"Peter Cassell": "05/05/1992",
}

print("Please enter a name and the program will output the corresponding birthday.")
print(bdaydict.keys())
choice = input()
print(bdaydict.get(choice, "No person of that name in the database"))


a= 5757
b= 8989
print("my number is {} and his number is {}".format(a, b)) #interesting means of formatting strings with embedded variables.

