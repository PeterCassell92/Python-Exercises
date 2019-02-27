#!usr/bin/python3
#This program opens a text file of the happy and prime numbers between 0 and 1000 and identifies the overlap in these lists.
with open('primenumbers.txt', 'r') as open_file:
	line = open_file.readline()
	primelist = []
	while line:
		primelist.append(line.strip())
		line = open_file.readline()


with open('happynumbers.txt', 'r') as open_file:
	line = open_file.readline()
	happylist = []
	while line:
		happylist.append(line.strip())
		line = open_file.readline()

c=[]

[c.append(elem) for elem in primelist if elem in happylist and elem not in c]

print(c)

