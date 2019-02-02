#!/usr/bin/python
import getpass

print("Welcome to Rock Paper Scissors")

player1 = ''
player2 = ''

print("Player 1 - SECRETLY enter your selection of R, P or S")
player1 = getpass.getpass("enter Key :")
print("Player 2 - SECRETLY enter your selection of R, P or S")
player2 = getpass.getpass("enter Key :")

if player1.lower() == player2.lower():
	print("The Game is a Tie.")

elif player1.lower() == 'r':
	if player2.lower() == 'p':
		print("Player 2's Paper wraps up Player 1's Rock")
	elif player2.lower() == 's':
		print("Player 1's Rock blunts Player 2's Scissors")
elif player1.lower() == 'p':
	if player2.lower() == 's':
		print("Player 2's Scissors cuts Player 1's Paper to shreds")
	elif player2.lower() == 'r':
		print("Player 1's Paper wraps up Player 2's Rock")
elif player1.lower() == 's':
	if player2.lower() == 'r':
		print("Player 2's Rock blunts Player 1's Scissors")
	elif player2.lower() == 'p':
		print("Player 1's Scissors cuts Player 2's Paper to shreds")



print("Finito")