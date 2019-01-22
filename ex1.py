#!/usr/bin/python
def yes_or_no(question):
    reply = str(raw_input(question+' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return True
    if reply[0] == 'n':
        return False
    else:
        return yes_or_no("Uhhhh... please enter ")

name = raw_input("What is your name?")
print("What is your age?")
age = input()

if yes_or_no("Have you had your birthday this year?"):
	correction = 0
else:
	correction = 1

print("How many instances?")
factor = input()

print type(factor)


centenary = (2019 -age - correction +100)
print(factor*("You will turn 100 in the year " + str(centenary)+"\n"))
