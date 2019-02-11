#!/usr/bin/python
def fibonnaci(num):
	a= [1]
	for i in range(1,num):
		
		if len(a) >= 2:
			prevsum = a[-1]+a[-2]

		if len(a) == 1:
			prevsum = a[0]

		a.append(prevsum)

	print(a)

fibonnaci(89)

