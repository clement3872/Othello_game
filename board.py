
# Note
# on est oblige de manger un pion lorsque l'on joue (i.e. c'est a l'autre de jouer)


def board_get(board_list, col, row):
	return board_list[row*8 + col]

def board_get_pos(col, row):
	return row*8 + col

def baord_get_direction_index(col,row, direction):
	# returns col and row for a certain direction
	if direction == "top" and row >= 1:
		row -= 1
	elif direction == "bottom" and row <= 6:
		row += 1
	elif direction == "left" and col >= 1:
		col -= 1
	elif direction == "right" and col <= 6:
		col += 1

	# diagonals
	elif direction == "top_left" and row >= 1 and col >= 1:
		row -= 1; col -= 1
	elif direction == "top_right" and row >= 1 and col <= 6:
		row -= 1; col += 1
	elif direction == "bottom_left" and row <= 6 and col >= 1:
		row += 1; col -= 1
	elif direction == "bottom_right" and row <= 6 and col <= 6:
		row += 1; col += 1

	return (col, row)


def possible_moves_from(board_list, col, row):
	"""moves you can do thanks to a pawn"""
	if col<0 or col>7 or row<0 or row>7: return board_list
	team = board_get(board_list, col, row)
	if team == 0: return board_list
	opposite_team = "white" if team=="black" else "black"

	def moves_rec(col, row, direction, points=0):
		current_pawn = board_get(board_list, col, row)
		tmp_col, tmp_row = col, row
		col,row = baord_get_direction_index(col,row, direction)

		# to avoid problems with recurtion
		if (tmp_col, tmp_row) == (col, row): return None 

		# pawn of the next position, depends on direction
		direc_pawn = board_get(board_list, col, row) 

		if current_pawn==opposite_team and type(direc_pawn)==type(int()):
			board_list[board_get_pos(col, row)] = points + direc_pawn
			# board_list[board_get_pos(col, row)] = points

		elif direc_pawn==opposite_team\
			and ((current_pawn==team and points==0)\
			or (points>0 and current_pawn==opposite_team)):
				moves_rec(col, row, direction, points+1)


		# elif direc_pawn==opposite_team and direc_pawn!=team:
		# 	moves_rec(col, row, direction, points+1)
		# else: return None

	for direction in ["top","bottom","left","right","top_left","top_right","bottom_left","bottom_right"]:
		moves_rec(col, row, direction)

	return board_list

def board_possible_moves(board_list, team):
	"""moves you can do thanks to all pawns"""
	def fusion(l1, l2):
		l = []
		for i in range(len(l1)):
			l.append(max(l1[i], l2[i]))
		return l

	for col in range(8):
		for row in range(8):
			pawn = board_get(board_list, col, row)
			if pawn != 0 and pawn==team:
				board_list = fusion(board_list, possible_moves_from(board_list, col, row))

	return board_list

def board_place_pawn(board_list, col, row, team):
	baord_get_direction_index(col,row, direction)



class Board(object):
	"""
	0 = empty
	"white" = white pawn
	"black" = black pawn
	n = points for a certain move
	"""

	def __init__(self, player_team="black"):
		self.player_team = player_team
		self.AI_team = "white" if player_team=="black" else "black"

		self.player_to_play = player_team == 2

		self.board_list = [
			0, 0, 0, 0, 0, 0, 0, 0,
			0, 0, 0, 0, 0, 0, 0, 0,
			0, 0, 0, 0, 0, 0, 0, 0,
			0, 0, 0, "white", "black", 0, 0, 0,
			0, 0, 0, "black", "white", 0, 0, 0,
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

		return board_possible_moves(board_list, team)


	def get_AI_move(self, board):
		# should we use this (?): 
		# https://fr.wikipedia.org/wiki/Algorithme_minimax 
		pass

	def udpate_board(self, new_board):
		self.board_list = new_board

	def update_with_possible_moves(self):
		self.board_list = board_possible_moves(self.board_list, self.player_team)

	def place_pawn(self, col, row):
		pass

	def get(self, col, row):
		return board_get(self.board_list, col, row)

	def calculate(self,row,col):
		print("Calculating...")

		print("Done calculating.")


# to test
if __name__ == '__main__':
	b = Board()
	# b.calculate(0,0)

	t = board_possible_moves(b.board_list, "black")
	for i in range(8):
		print(t[i*8:(i+1)*8])