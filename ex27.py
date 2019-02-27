#!/usr/bin/python
def analysetictactoe(boardlist):
	if len(boardlist) != 3:
		return print("The list submitted does not represent a tic tac toe board")

	for x in range(0,3):
		if boardlist[x][1] == boardlist[x][2] == boardlist[x][0] !=0:
			return True, boardlist[x][0]

	for x in range(0,3):
		if boardlist[0][x] == boardlist[1][x] == boardlist[2][x] !=0 :
			return True, boardlist[0][x]

	if boardlist[0][0] == boardlist[1][1] == boardlist [2][2] != 0 or boardlist[2][0] == boardlist[1][1] == boardlist[0][2] != 0:
		return True, boardlist[1][1]

	a=0
	for sublist in boardlist:
		if 0 not in sublist:
			a +=1
			if a == 3:
				return True, "Draw"

	return False, ""


gameboard=[ [0,0,0], [0,0,0],[0,0,0]]
turn = 1
roundno =1
gameend = False
winner = ""
print(str(gameboard[0]) + "\n" + str(gameboard[1]) + "\n" + str(gameboard[2]))
print("The top left cell is 1,1 and bottom right cell is 3,3")

while gameend == False:
	print("Player " + str(turn) + " input the coordinates to place your marker in format \"x,y\"" )
	playerinput = str(input())
	xcoord = int(playerinput[2])-1
	ycoord = int(playerinput[0])-1

	if turn ==1:
		if gameboard[xcoord][ycoord] == 0:
			gameboard[xcoord][ycoord] = "X"
			turn = 2
		else:
			print("Space already occupied")
	elif turn == 2:
		if gameboard[xcoord][ycoord] == 0:
			gameboard[xcoord][ycoord] = "O"
			turn =1
			roundno +=1
		else:
			print("Space already occupied")

	gameend, winner = analysetictactoe(gameboard)
	print(gameend)
	
	print(str(gameboard[0]) + "\n" + str(gameboard[1]) + "\n" + str(gameboard[2]))


print("Game Complete")
print(winner)



	