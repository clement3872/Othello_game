import subprocess
# import os 

class Board(object):
	"""
	0 = empty
	1 = white pawn
	2 = black pawn
	3 = possible moves 
	"""

	def __init__(self, player_team="black"):

		self.player_team = 2 if player_team=="black" else 1
		self.AI_team = 1 if player_team=="black" else 2

		self.board_list = [
			0, 0, 0, 0, 0, 0, 0, 0,
			0, 0, 0, 0, 0, 0, 0, 0,
			0, 0, 0, 0, 0, 0, 0, 0,
			0, 0, 0, 1, 2, 0, 0, 0,
			0, 0, 0, 2, 1, 0, 0, 0,
			0, 0, 0, 0, 0, 0, 0, 0,
			0, 0, 0, 0, 0, 0, 0, 0,
			0, 0, 0, 0, 0, 0, 0, 0
		]

	def get(self, row, col):
		return self.board_list[row*8 + col]

	def calculate(self,i,j):
		print("Calculating...")

		print("Done calculating.")


# to test
if __name__ == '__main__':
	b = Board()
	b.calculate(0,0)
