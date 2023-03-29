"""
Created By: Viktor Dominguez
Tested By: Viktor Dominguez
Date Started: 02/12/2023 (mm/dd/yyyy)
Last Updated: 02/12/2023 (mm/dd/yyyy)
Editor: Sublime Text

------------
DESCRIPTION
------------

Create a Yugi-oh game script that will take in starting conditions (such as players, life points, maybe display their health as "bars" (=), and who's turn it is)
NOTE --> NOT a Yugi-oh simulator, just used to keep track of LP for 2 players
Inspiration was from not wanting to keep track of our LP on our phones and constantly have to ask how many we had left


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

# Function to clear the screen
def clear():
	os.system('cls' if os.name == 'nt' else 'clear')


# Delayed Text Output Function
def delay_readout(string):
	for char in string:
		sys.stdout.write(char)
		sys.stdout.flush()
		sleep(0.05)


class player:
	def __init__(self, name, lifepoints=8000):
		self.name = name
		self.lifepoints = lifepoints
		# Display of health bars (=)
		self.health = "="*20
		# Bars will always mod to 20
		self.bars = 20

	def playerturn(self, player2):
		clear()
		delay_readout(f"It is {self.name}'s turn!")
		print(f"\n\n\t\t{self.name}'s Life Points: {self.lifepoints}\t\t{self.health}")
		print(f"\n\t\t{player2.name}'s Life Points: {player2.lifepoints}\t\t{player2.health}\n\n")
		print("*"*40)
		delay_readout(f"\n\n{self.name} attacks! Enter your attack power: ")
		attack = int(input())
	


if __name__ == '__main__':
	pass