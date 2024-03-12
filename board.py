
# Note
# on est oblige de manger un pion lorsque l'on joue (i.e. c'est a l'autre de jouer)


def board_get(board_list, col, row):
	return board_list[row*8 + col]

def board_get_pos(col, row):
	return row*8 + col

def board_get_points(board_list, col, row):
	team = board_get(board_list, col, row)
	# ...

def possible_moves_from(board_list, col, row):
	if col<0 or col>7 or row<0 or row>7: return board_list
	team = board_get(board_list, col, row)
	if team == 0: return board_list
	possible_move_color = 3 if team == 1 else 4

	def moves_rec(col, row, direction):
		current_team = board_get(board_list, col, row)
		checked = False
		if direction == "top" and row >= 1:
			row -= 1; checked = True
		elif direction == "bottom" and row <= 6:
			row += 1; checked = True
		elif direction == "left" and col >= 1:
			col -= 1; checked = True
		elif direction == "right" and col <= 6:
			col += 1; checked = True

		elif direction == "top_left" and row >= 1 and col >= 1:
			row -= 1; col -= 1; checked = True
		elif direction == "top_right" and row >= 1 and col <= 6:
			row -= 1; col += 1; checked = True
		elif direction == "bottom_left" and row <= 6 and col >= 1:
			row += 1; col -= 1; checked = True
		elif direction == "bottom_right" and row <= 6 and col <= 6:
			row += 1; col += 1; checked = True

		if checked:
			# pawn of the next position, depends on direction
			direc_pawn = board_get(board_list, col, row) 
			if (current_team != team and direc_pawn==0) or direc_pawn==possible_move_color:
				board_list[board_get_pos(col, row)] = possible_move_color
			elif direc_pawn != current_team and direc_pawn != 0:
				return moves_rec(col, row, direction)

		return board_list

	def fusion(l1, l2):
		l = []
		for i in range(len(l1)):
			l.append(max(l1[i], l2[i]))
		return l

	board_list = moves_rec(col, row, "top")
	board_list = fusion(board_list, moves_rec(col, row, "bottom"))
	board_list = fusion(board_list, moves_rec(col, row, "left"))
	board_list = fusion(board_list, moves_rec(col, row, "right"))

	board_list = fusion(board_list, moves_rec(col, row, "top_left"))
	board_list = fusion(board_list, moves_rec(col, row, "top_right"))
	board_list = fusion(board_list, moves_rec(col, row, "bottom_left"))
	board_list = fusion(board_list, moves_rec(col, row, "bottom_right"))

	return board_list

def board_possible_moves(board_list, team):
	"""
	team -> type: int, team in [1,2]
	"""
	for col in range(8):
		for row in range(8):
			pawn = board_get(board_list, col, row)
			if pawn != 0 and pawn==team:
				board_list = possible_moves_from(board_list, col, row)

	return board_list


class Board(object):
	"""
	0 = empty
	1 = white pawn
	2 = black pawn
	3 = possible moves for white
	4 = possible moves for black
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

	def possible_moves(self, team="player", board_list=None):
		"""returns a board_list of the possible moves
		team -> type: String
		baord -> type: None or list
		"""

		if board_list == None: board_list = self.board_list

		if team == "player": team = self.player_team
		else: team = self.AI_team


	def get_AI_move(self, board):
		# should we use this (?): 
		# https://fr.wikipedia.org/wiki/Algorithme_minimax 
		pass

	def udpate_board(self, new_board):
		self.board_list = new_board

	def get(self, col, row):
		return board_get(self.board_list, col, row)

	def calculate(self,row,col):
		print("Calculating...")

		print("Done calculating.")


# to test
if __name__ == '__main__':
	b = Board()
	# b.calculate(0,0)

	t = possible_moves_from(b.board_list, 3,4)
	for i in range(8):
		print(t[i*8:(i+1)*8])