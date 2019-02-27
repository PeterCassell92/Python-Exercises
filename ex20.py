#!usr/bin/python3




def verifynuminlist(integer, mylist):
	truth_value = integer in mylist
	if truth_value:
		print(str(integer) + " IS present in the list.")
	else:
		print(str(integer) + " IS NOT present in the list.")


if __name__=="__main__":

	mylist = [1,4,8,9,11,14,57,67,79]
	verifynuminlist(9 ,mylist)
	verifynuminlist(1 ,mylist)
	verifynuminlist(12 ,mylist)
	verifynuminlist(19 ,mylist)
	verifynuminlist(57 ,mylist)

