#!/usr/bin/python
#This program will find the first and last elements of a list.s

a = [5, 10, 15, 20, 25]


def findFirstlastoflist(mylist):
	b= [mylist[0], mylist[-1]]
	return b

print(findFirstlastoflist(a))