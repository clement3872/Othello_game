import board
    # Initialize the board_list

# Function to print the board_list
def print_board_list(board_list):
    for i in range(8):
        t = []
        for j in range(8):
            t.append(board_list[i*8+j])
    print("####")  # Print a separator to indicate the end of the board print

# Function to check if a move is within board limits
def in_bound(x, y):
    return 0 <= x < 8 and 0 <= y < 8

# Function to get all valid moves for a player
def get_valid_moves(board_list, player_team):
    valid_moves = []
    for x in range(8):
        for y in range(8):
            # Ensure the move is not on a spot already occupied by black, white, or empty
            if board_list[board.board_get_pos(x, y)] not in ("black", "white", 0):
                valid_moves.append((x, y))
    return valid_moves

# Function to apply a move on the board_list
def apply_move(board_list, player_team, x, y):
    if player_team == "black":
        AI_team = "white"
    else:
        AI_team = "black"
    
    board_list[board.board_get_pos(x, y)] = player_team
    # Flip opponent's pieces
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dx, dy in directions:
        temp_x, temp_y = x + dx, y + dy
        if in_bound(temp_x, temp_y) and board_list[board.board_get_pos(temp_x, temp_y)] == AI_team:
            while board_list[board.board_get_pos(temp_x, temp_y)] == AI_team:
                temp_x += dx
                temp_y += dy
                if not in_bound(temp_x, temp_y):
                    break
            if in_bound(temp_x, temp_y) and board_list[board.board_get_pos(temp_x, temp_y)] == player_team:
                while (temp_x, temp_y) != (x, y):
                    temp_x -= dx
                    temp_y -= dy
                    board_list[board.board_get_pos(temp_x, temp_y)] = player_team

# Evaluation function
def get_score(board_list, player_team):
    # Simple evaluation function: count the difference in number of pieces
    if player_team == "black":
        AI_team = "white"
    else:
        AI_team = "black"
    
    player_count = board_list.count(player_team)
    opponent_count = board_list.count(AI_team)
    return player_count - opponent_count

# Minimax with Alpha-Beta Pruning
def minimax(board_list, depth, player_team, alpha, beta):
    if player_team == "black":
        AI_team = "white"
    else:
        AI_team = "black"

    if depth == 0:
        return get_score(board_list, player_team), None
    valid_moves = get_valid_moves(board_list, player_team)
    if not valid_moves:
        return get_score(board_list, player_team), None
    
    best_move = None
    if player_team == "black":  # Maximizing player
        max_score = -999
        for move in valid_moves:
            new_board_list = [row for row in board_list]
            apply_move(new_board_list, player_team, *move)
            score, _ = minimax(new_board_list, depth - 1, AI_team, alpha, beta)
            if score > max_score:
                max_score = score
                best_move = move
            alpha = max(alpha, score)
            if alpha >= beta:
                break
        return max_score, best_move
    
    else:  # Minimizing player
        min_score = 999
        for move in valid_moves:
            new_board_list = [row for row in board_list]
            apply_move(new_board_list, player_team, *move)
            score, _ = minimax(new_board_list, depth - 1, AI_team, alpha, beta)
            if score < min_score:
                min_score = score
                best_move = move
            beta = min(beta, score)
            if beta <= alpha:
                break
        return min_score, best_move

# Example of how to use the functions
# Assume "black" starts first
if __name__ == "__main__":
    # Initial board setup
    board_list = [
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, "white", "black", 0, 0, 0,
    0, 0, 0, "black", "white", 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0
    ]
    player_team = "black"
    AI_team = "white"

    while True:
        # Update and display the board with possible moves
        board_list = board.board_possible_moves(board_list, player_team)
        for i in range(8):
            print(board_list[i*8:(i+1)*8])
        print_board_list(board_list)
        # If it's AI's turn
        if player_team == "white":
            x, y = minimax(board_list, 8, player_team, -999, 999)[1]  # Depth 8
            apply_move(board_list, player_team, x, y)
        else:
            # Request and apply the human player's move
            print("Enter your move (column then row): ")
            x, y = int(input()), int(input())
            apply_move(board_list, player_team, x, y)
        # Clean the board and switch players
        board_list = board.board_clean(board_list)
        player_team, AI_team = AI_team, player_team  # Switch players
