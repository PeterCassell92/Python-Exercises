#!usr/bin/python3
import random

def stringfrequencyinlist(mylist,string):
	return str(mylist.count(string))


if __name__=="__main__":    
	
	hiddennum1 = random.sample(range(0,9), 4)
	hiddennum = str(hiddennum1[0]) + str(hiddennum1[1]) + str(hiddennum1[2]) + str(hiddennum1[3])

	print("Welcome to Cows & Bulls.\r\nThe computer has generated a four digit number composed of unique digits. \r\n You must guess this number in as few trys as possible. ")
	x=1
	finished = False
	while finished == False:
		match=["","","",""]
		guess= str((input("Enter your 4 digit integer guess or type EXIT to quit.  \"\" %s: " % (x))))

		if guess == "EXIT":
			finished= True

		
		for y in range (4):
			for z in range (4):
				if guess[y] == hiddennum[z]: 
					if match[y] != "Cow":
						if guess[y] == hiddennum[y] :
							match[y]= "Cow"
						else :
							match[y]= "Bull"
						if match == ["Cow","Cow","Cow","Cow"]:
							print("You have finished correctly!! Well done!")
							finished = True

		bullcount = stringfrequencyinlist(match, "Bull")
		cowcount = stringfrequencyinlist(match, "Cow")
		print("Cows = " + cowcount + "\r\n" + "Bulls = " +bullcount + "\r\n" + "No. of Guesses = " + str(x))
		x +=1

	print("The correct answer was %s" % hiddennum)