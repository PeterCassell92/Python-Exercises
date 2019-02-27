#!usr/bin/python3
with open('ex22namelist.txt', 'r') as open_file:
	line = open_file.readline()
	namelist = []
	while line:
		namelist.append(line.strip())
		line = open_file.readline()

print(namelist)

print(str(namelist.count('Luke')) + " Lukes")
print(str(namelist.count('Lea')) + " Leas")
print(str(namelist.count('Darth')) + " Darths")