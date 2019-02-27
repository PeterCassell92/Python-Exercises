#!/usr/bin/python3
#The computer will analyse the winner of the tic tac toe boards represented as a list of three lists.

winner_is_2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_1 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

also_no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]

def analysetictactoe(boardlist):
	if len(boardlist) != 3:
		return print("The list submitted does not represent a tic tac toe board")

	for x in range(0,2):
		if boardlist[x][1] == boardlist[x][2] == boardlist[x][0]:
			return print("match in row " + str(x)+".\n Winner is player " +str(boardlist[x][0])+ "\n")

	for x in range(0,2):
		if boardlist[0][x] == boardlist[1][x] == boardlist[2][x]:
			return print("match in column " + str(x) +".\n Winner is player " +str(boardlist[2][x]) + "\n")

	if boardlist[0][0] == boardlist[1][1] == boardlist [2][2] or boardlist[2][0] == boardlist[1][1] == boardlist[0][2]:
		return print ("Diagonal match " + str(x) +".\n Winner is player " +str(boardlist[1][1]) + "\n")

	return print("There is no current winner on this Tic Tac Toe Board \n")



analysetictactoe(winner_is_2)
analysetictactoe(winner_is_1)
analysetictactoe(winner_is_also_1)
analysetictactoe(also_no_winner)
analysetictactoe(no_winner)