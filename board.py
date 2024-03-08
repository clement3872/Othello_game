
# Note
# on est oblige de manger un pion lorsque l'on joue (i.e. c'est a l'autre de jouer)

class Board(object):
	"""
	0 = empty
	1 = white pawn
	2 = black pawn
	3 = possible moves for player
	4 = possible moves for AI
	"""

	def __init__(self, player_team="black"):
		self.player_team = 2 if player_team=="black" else 1
		self.AI_team = 1 if player_team=="black" else 2

		self.player_to_play = player_team == 2

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


	def get_points(self, col, row, board):
		"""get points for a certain move"""
		pass

	def possible_moves(self, board):
		"""returns a board_list of the possible moves"""
		pass

	def get_AI_move(self, board):
		# should we use this (?): 
		# https://fr.wikipedia.org/wiki/Algorithme_minimax 
		pass

	def udpate_board(self, new_board):
		self.board_list = new_board

	def get(self, col, row):
		return self.board_list[row*8 + col]

	def calculate(self,row,col):
		print("Calculating...")

		print("Done calculating.")


# to test
if __name__ == '__main__':
	b = Board()
	b.calculate(0,0)
