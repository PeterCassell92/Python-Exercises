#!/usr/bin/python
import random

a=[]
b=[]
lengtha = random.randint(5,20)
lengthb = random.randint(5,20)
for x in range(0,lengtha):
	a.append(random.randint(1,20))
for x in range(0,lengthb):
	b.append(random.randint(1,20))


print(a)
print(b)

c=[]

[c.append(elem) for elem in a if elem in b and elem not in c]

c.sort()


print(c)