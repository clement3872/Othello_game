import ai

def board_get(board_list, col, row):
    """Retrieve the element at specified coordinates in the board_list."""
    return board_list[row*8 + col]

def board_get_pos(col, row):
    """Calculate the linear index in the board_list based on column and row coordinates."""
    return row*8 + col

def board_get_direction_index(col, row, direction):
    """Update column and row based on the specified direction."""
    if direction == "top" and row >= 1:
        row -= 1
    elif direction == "bottom" and row <= 6:
        row += 1
    elif direction == "left" and col >= 1:
        col -= 1
    elif direction == "right" and col <= 6:
        col += 1

    # Handling diagonal movements
    elif direction == "top_left" and row >= 1 and col >= 1:
        row -= 1; col -= 1
    elif direction == "top_right" and row >= 1 and col <= 6:
        row -= 1; col += 1
    elif direction == "bottom_left" and row <= 6 and col >= 1:
        row += 1; col -= 1
    elif direction == "bottom_right" and row <= 6 and col <= 6:
        row += 1; col += 1
    return (col, row)

def coords_in_bounds(col, row, direction):
	"""Check if the coordinates after a move in the given direction are still within board bounds."""
 
	if direction == "top": return row >= 1
	elif direction == "bottom": return row <= 6
	elif direction == "left": return col >= 1
	elif direction == "right": return col <= 6

	# diagonals
	elif direction == "top_left": return row >= 1 and col >= 1
	elif direction == "top_right": return row >= 1 and col <= 6
	elif direction == "bottom_left": return row <= 6 and col >= 1
	elif direction == "bottom_right": return row <= 6 and col <= 6
	else: return False # should never happen


def possible_moves_from(board_list, col, row):
	"""Determine all possible moves from a given pawn's position."""
	if col<0 or col>7 or row<0 or row>7: 
		return board_list
	team = board_get(board_list, col, row)
	if team == 0: 	# No pawn to move
		return board_list 
	opposite_team = "white" if team=="black" else "black"

	def moves_rec(col, row, direction, points=0):
		"""Recursively find and mark all valid moves."""
		current_pawn = board_get(board_list, col, row)

		# stop the recursion
		if not coords_in_bounds(col, row, direction):
			return None

		# pawn of the next position, depends on the direction
		col,row = board_get_direction_index(col,row, direction)
		direc_pawn = board_get(board_list, col, row) 

		# if we can place a pawn at the next coordinates
		if current_pawn==opposite_team and type(direc_pawn)==type(int()):
			board_list[board_get_pos(col, row)] = points + direc_pawn

		# if we don't know if we can place a pawn at the next coordinates
		elif direc_pawn==opposite_team:
			moves_rec(col, row, direction, points+1)


	for direction in ("top","bottom","left","right","top_left","top_right","bottom_left","bottom_right"):
		moves_rec(col, row, direction)

	return board_list


def board_possible_moves(board_list, team):
	"""moves you can do thanks with every pawns
	-
	Returns the board_list, possible moves are as other numbers than 0,
	these numbers are the points that a certain move grants
	-
	team -> type: String
	baord -> type: None or list
	"""

	for col in range(8):
		for row in range(8):
			pawn = board_get(board_list, col, row)
			if pawn != 0 and pawn==team:
				board_list = possible_moves_from(board_list, col, row)

	return board_list

def coords_out_of_bound_place(col, row):
	"""Check if the coordinates are out of playable board boundaries."""
	return col<1 or col>6 or row<1 or row>6

def board_place_pawn(board_list, col, row, ally_team):
	"""
	Does what is says: place a pawn at the desired coordinates, and turns all pawns needed
	"""

	opposite_team = "white" if ally_team=="black" else "black"

	for direction in ["top","bottom","left","right","top_left","top_right","bottom_left","bottom_right"]:
		tmp_col, tmp_row = board_get_direction_index(col,row, direction)

		# checking if we can turn pawns in the direction
		while board_get(board_list, tmp_col, tmp_row) == opposite_team\
		and coords_in_bounds(tmp_col, tmp_row, direction):
			tmp_col, tmp_row = board_get_direction_index(tmp_col, tmp_row, direction)

		# turning the pawns if we actually can
		if board_get(board_list, tmp_col, tmp_row) == ally_team:
			# possible_directions.append(direction)
			tmp_col, tmp_row = board_get_direction_index(col,row, direction)
			while board_get(board_list, tmp_col, tmp_row) == opposite_team:
				board_list[board_get_pos(tmp_col, tmp_row)] = ally_team
				board_list[board_get_pos(col,row)] = ally_team
				tmp_col, tmp_row = board_get_direction_index(tmp_col, tmp_row, direction)

	return board_list

def board_clean(board_list):
	"""Remove all non-pawn elements from the board."""
	for i in range(len(board_list)):
		if board_list[i] not in ("white", "black"): 
			board_list[i] = 0

	return board_list


def board_get_AI_move(board_list, AI_team):
	"""Calculate the best move for AI using the minimax algorithm."""
	board_list = board_possible_moves(board_list,AI_team)
	res = ai.minimax(board_list, 8, AI_team, -999, 999)[1] # Depth 8
	if res == None:
		# random possible move because of minmax issue at the end of game
		for i_col in range(8):
			for i_row in range(8):
				pawn = board_get(board_list, i_col, i_row)
				if pawn not in ("white", "black",0):
					col, row = i_col, i_row 
					return board_clean(board_place_pawn(board_list, col, row, AI_team))
		return board_clean(board_list)
	else:
		col, row = res
		return board_clean(board_place_pawn(board_list, col, row, AI_team))

def board_is_full(board_list):
	"""Check if the board has no empty spaces left."""
	for pawn in board_list:
		if pawn not in ["black", "white"]:
			return False
	return True


class Board(object):
	"""
	0 = empty
	"white" = white pawn
	"black" = black pawn
	n = points for a certain move
	nb_player = 1 for AI
	nb_player = 2 for p vs p
	"""

	def __init__(self, nb_players=1, player_team="black"):
		self.nb_players = nb_players
		self.player_team = player_team
		self.AI_team = "white" if player_team=="black" else "black"
		self.unplayble_round = 0
	
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

		self.history = []  # Initialize empty history list

	def possible_moves(self, team="player", board_list=None):
		"""
		Returns the board_list, possible moves are as other numbers than 0,
		these numbers are the points that a certain move grants
		-
		team -> type: String
		baord -> type: None or list
		"""

		if board_list == None: board_list = self.board_list

		if team == "player": team = self.player_team
		else: team = self.AI_team

		return board_possible_moves(board_list, team)

	def get_AI_move(self):
		"""Does what is says"""
		board_list = board_get_AI_move(self.board_list, self.AI_team)
		return board_list

	def update_with_possible_moves(self):
		"""Update the board with possible moves highlighted."""
		self.board_list = self.possible_moves()

	def clean(self):
		"""Clean the board, removing highlights and only leaving pawns."""
		self.board_list = board_clean(self.board_list)

	def place_pawn(self, col, row, team=None):
		""" function shoud be used for the interface.py
		team in (None, "white", "black"), None = player_team
		-
		This function updates the board_list for a certain move
		"""

		team = self.player_team
		if team is None or self.nb_players == 2: 
			self.player_team = self.AI_team
			self.AI_team = team

		self.history.append(self.board_list.copy())
		self.board_list = board_place_pawn(self.board_list, col, row, team)
		self.clean()
		if self.nb_players == 1 and not self.is_full():
			self.board_list = self.get_AI_move() 
			self.clean()
		self.update_with_possible_moves()

		# if player vs AI, AI plays if player can't
		while not self.is_playable() and not self.is_full() and self.nb_players==1:
			self.clean()
			self.board_list = self.get_AI_move() 
			self.clean()
			self.update_with_possible_moves()

		# if player vs player, we skip the turn 
		if self.nb_players == 2 and not self.is_playable():
			self.player_team,self.AI_team = self.AI_team,self.player_team
			self.clean()
			self.update_with_possible_moves()

		self.is_playable() 

	def get(self, col, row):
		"""Get the element at the specified position on the board."""
		return board_get(self.board_list, col, row)

	def is_playable(self):
		"""Checks if there are any playable moves remaining for the current player.

		Returns:
			bool: True if there are playable moves, False otherwise.
		"""
		for el in self.board_list:
			if el not in ("black", "white") and el > 0:
				self.unplayble_round = 0
				return True
		self.unplayble_round += 1
		return False

	def undo(self):
		"""Undo the last move made by the current player."""
		if self.history:
			last_board = self.history.pop()
			self.board_list = last_board
			return True
		else:
			return False
		
	def is_full(self):
		"""Check if the board is fully occupied."""
		return board_is_full(self.board_list)
		# for pawn in self.board_list:
		# 	if pawn not in ["black", "white"]:
		# 		return False
		# return True
		

# to test
if __name__ == '__main__':
	b = Board()
	# b.calculate(0,0)

	t = board_possible_moves(b.board_list, "black")
	for i in range(8):
		print(t[i*8:(i+1)*8]) # Display each row of the board