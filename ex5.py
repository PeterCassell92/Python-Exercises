#!/usr/bin/python
a=[4,5,9,10,15,18,25,29]
b=[9,15,7,4,39,22,29,16]
c=[]

for ax in a:
	if ax in b:
		c.append(ax)

print(c)