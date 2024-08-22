"""
Created By: Viktor Dominguez
Tested By: Viktor Dominguez
Date Started: 02/12/2023 (mm/dd/yyyy)
Last Updated: 08/21/2024 (mm/dd/yyyy)
Initial Editor: Sublime Text
Final Editor: Visual Studio Code

------------
DESCRIPTION
------------

Create a Yugi-oh game script that will take in starting conditions (such as players, life points, maybe display their health as "bars" (=), and who's turn it is).
NOTE --> NOT a Yugi-oh simulator, just used to keep track of the life points for 2 players.
Inspiration was from not wanting to keep track of our life points on our phones and constantly have to ask how many we had left.


## IGNORE IF YOU JUST WANT TO SEE THE CODE ##
---------------
BRAINSTORMING
---------------

- class object for each player (store the LP, names, and amount of health bars left in here)
	* Health bar for standard game: 20 Bars? (for 8000 LP: 400 LP == 1 Bar)
- Game() function takes in two player objects and sets their parameters (LP and names)
	* Recall Game() until one player reaches 0 LP (recursive)
	* Maybe add a loop to ask if the player wants to play again?
- Life Points standard = 8000; give player option to set this at the beginning (sets for both players)
- Need to determine who goes first? Or just in order that they're entered in?

"""

from random import randint
import sys
from time import sleep
import os
#
#
# Function to clear the screen
def clear():
	os.system('cls' if os.name == 'nt' else 'clear')
#
#
# Delayed Text Output Function
def delay_readout(string):
	for char in string:
		sys.stdout.write(char)
		sys.stdout.flush()
		sleep(0.05)
#
class player:
	def __init__(self, name, lifepoints = 8000, defense = 0):
		# Will use starting value to calculate health bars
		self.startingPoints = lifepoints
		self.name = name
		self.lifepoints = lifepoints
		# Display of health bars (=)
		self.health = "="*20
		# Bars will always mod to 20
		self.bars = 20
		# Defense of monsters
		self.defense = defense
#
	# Player's turn function
	def playerturn(self, player2):
		# Main status display: players, health, and LP remaining
		delay_readout(f"\n\nIt is {self.name}'s turn!")
		sleep(1.2)
		print(f"\n\n{self.name}'s Life Points: {self.lifepoints}\t\t{self.health}")
		print(f"\n\n{player2.name}'s Life Points: {player2.lifepoints}\t\t{player2.health}\n\n")
		print("*"*100)
		sleep(2.0)
#
		while True:
			print(f"\n\nPlease enter in {player2.name}'s defense points: ")
			try:
				player2.defense = int(input())
				break
			except ValueError:
				delay_readout(f"\n\nYou have entered an invalid value.")
				continue
		while True:
			print(f"\n\nEnter {self.name}'s' attack's power: ")
			try:
				attack = int(input())
				break
			except ValueError:
				print(f"\n\nPlease enter in a valid number")
		total = attack - player2.defense
		if total <= 0:
			delay_readout(f"\n\n{self.name} failed to inflict any damage to {player2.name}'s life points.")
			sleep(1.2)
			return
		player2.lifepoints -= total
		# Want the percentage of lifepoints left * 20 bars 
		player2.bars = max(1, (player2.lifepoints/player2.startingPoints)*20)
		player2.health = "="*int(player2.bars)
		print(f"\n\n{self.name} attacked for {total} damage.")
		sleep(1.2)

if __name__ == '__main__':
	while True:
		delay_readout("\nEnter the starting lifepoints or hit ENTER for the default: ")
		try:
			startValue = int(input())
		except ValueError:
			delay_readout("\n\nThe default value will be used.")
			# Default value = 8000
			startValue = 8000
		delay_readout("\n\nPlease enter Player 1's Name: ")
		name1 = input()
		player1 = player(name1, startValue)
		sleep(1.2)
		delay_readout("\n\nPlease enter Player 2's Name: ")
		name2 = input()		
		player2 = player(name2, startValue)
		sleep(1.2)


		def game(player1, player2):
			clear()
			delay_readout("\n\nIt's time to d-d-d-d-d-d-duel!")
			while player1.lifepoints and player2.lifepoints > 0:
				player1.playerturn(player2)
				if player2.lifepoints <= 0:
					delay_readout(f"\n\n{player1.name} wins!\n\n")
					break
				player2.playerturn(player1)
				if player1.lifepoints <= 0:
					delay_readout(f"\n\n{player2.name} wins!\n\n")
					break
		game(player1, player2)
		sleep(5.0)
		while True:
			clear()
			delay_readout(f"That was fun! Care for another round? ")
			try:
				rematch = input()
				if rematch.isalpha() and rematch[0].lower() == 'y' or rematch[0].lower() == 'n' :
					break
				else:
					raise TypeError
			except TypeError:
				delay_readout("\n\nPlease enter 'yes'/'no' or 'y'/'n' to continue.")
				sleep(2.0)
		if rematch[0].lower() == 'n':
			break
	delay_readout("\n\nSo long! Nice playing!")
	sleep(1.5)
	clear()
