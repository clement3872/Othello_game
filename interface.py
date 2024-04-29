import pickle
import tkinter as tk
from tkinter import *
from tkinter import messagebox as tkm
import board 
import launcher as minter
import musik as mk

# Definition of Interface class that inherits Tk from tkinter
class Interface(Tk):
    def __init__(self, nb_players, player_team="black"):
        super().__init__()

        self.game_board = board.Board(nb_players, player_team)
        if nb_players == 1 and player_team == "white":
            self.game_board.board_list = self.game_board.get_AI_move()
        self.b_score = self.game_board.board_list.count("black")
        self.w_score = self.game_board.board_list.count("white")

        self.width, self.height = 600, 600 # Canvas size
        self.minsize(width=600, height=700)
        self.maxsize(width=600, height=700)

        # Calculating the size of each square on the board
        self.size_x = self.width // 8
        self.size_y = self.height // 8
        # Initializing player scores
        self.player_scores = {"black": 2, "white": 2}

        # Setting the window title
        self.title("Plateau de l'Othello")

        # Creation of the canvas for the game
        self.canvas = tk.Canvas(self, width=self.width, height=self.height, bg="#21854d")
        self.canvas.pack()

        # Binding left mouse click
        self.canvas.bind("<Button-1>", self.on_click)
        
        # A button to undo the last move
        self.undo_button = tk.Button(self, text="Undo", command=self.undo_move)
        self.undo_button.pack(side=tk.LEFT)

        # Current team display
        self.label_display = tk.Label(self, text=self.game_board.player_team)
        self.protocol('WM_DELETE_WINDOW', self.return_main)

        # Updating and displaying the initial board setup
        self.game_board.update_with_possible_moves()
        self.display_grid()
        self.display_pawns()

        # Button to exit the game
        self.ret = tk.Button(self, text="Quit", command=self.return_main)
        self.ret.pack()

        # Button to load the game
        self.load_button = tk.Button(self, text="Load", command=self.load)
        self.load_button.pack()

        # Button to save the game
        self.save_button = tk.Button(self, text="Save", command=self.save)
        self.save_button.pack()

        # Option to enable/disable music
        self.check_button_music = tk.BooleanVar(value=(mk.music_player.music_on == False))
        self.check_button_m = tk.Checkbutton(self, text="Mute", variable=self.check_button_music, command=mk.music_player.switch_board)
        self.check_button_m.place(x=500, y=650)

        # Displaying player scores
        self.score_blk = tk.Label(self, text="Black: " + str(self.player_scores["black"]))
        self.score_wht = tk.Label(self, text="White: " + str(self.player_scores["white"]))
        self.score_blk.pack(side=tk.LEFT)
        self.score_wht.pack(side=tk.LEFT)

    def return_main(self):
        """Handles the event when the window is closed"""
        self.destroy()
        mk.music_player.swap_interface()
        minter.Main_Interface()

    def on_click(self, event):
        """Handles click events on the canvas"""
        x, y = event.x // self.size_x, event.y // self.size_y
        if self.game_board.get(x, y) == 0 or self.game_board.get(x, y) in ("white", "black"):
            self.label_display.pack_forget()
            self.label_display = tk.Label(self, text="you cannot play here")
            self.label_display.pack()
            return 1

        self.game_board.place_pawn(x, y)
        self.label_display.pack_forget()
        self.label_display = tk.Label(self, text=self.game_board.player_team)
        self.label_display.pack()

        self.clear_canvas()
        self.display_grid()
        self.display_pawns()
        self.check_board_is_full()
        self.update_score()

    def clear_canvas(self):
        """Removes everything on the canvas"""
        self.canvas.delete("all")
        self.display_grid()

    def display_pawns(self):
        """Display pawns on the canvas"""
        # "radius" for the pawns
        pawn_size_x = self.size_x//2.5
        pawn_size_y = self.size_y//2.5
        # To place the pawns in the center of a box
        half_box_x = self.size_x//2
        half_box_y = self.size_y//2

        for i in range(8):  # column
            for j in range(8):  # row
                pawn = self.game_board.get(i, j)
                if pawn in ("white", "black"):
                    color = pawn
                    self.canvas.create_oval(
                        self.size_x * i - pawn_size_x + half_box_x,
                        self.size_y * j - pawn_size_y + half_box_y,
                        self.size_x * i + pawn_size_x + half_box_x,
                        self.size_y * j + pawn_size_y + half_box_y,
                        fill=color, outline=color)
                elif pawn > 0:
                    # Marker for possible moves
                    self.canvas.create_oval(
                        self.size_x * i - pawn_size_x // 2 + half_box_x,
                        self.size_y * j - pawn_size_y // 2 + half_box_y,
                        self.size_x * i + pawn_size_x // 2 + half_box_x,
                        self.size_y * j + pawn_size_y // 2 + half_box_y,
                        fill="gray", outline="orange")

    def display_grid(self):
        """Draws the lines of the grid on the canvas"""
        for i in range(1, 8):
            tmp_x = self.size_x * i
            tmp_y = self.size_y * i
            self.canvas.create_line(tmp_x, 0, tmp_x, self.height, width=3)
            self.canvas.create_line(0, tmp_y, self.width, tmp_y, width=3)

    def check_board_is_full(self):
        """Checks if the board is full and displays the winner"""
        if self.game_board.is_full():
            if self.b_score > self.w_score:
                tkm.showinfo("Winner", "Blacks won")
            elif self.b_score < self.w_score:
                tkm.showinfo("Winner", "Whites won")
            else:
                tkm.showinfo("Winner", "Draw")


    def undo_move(self):
        """Undo the last move if possible"""
        if self.game_board.undo():
            self.clear_canvas()
            self.display_pawns()
            self.update_score()
        else:
            tkm.showinfo("No Moves to undo", "There are no moves to undo.")

    def update_score(self):
        """
        For each move, calculate the number of occurrences of pawns in the list
        """
        self.b_score = self.game_board.board_list.count("black")
        self.w_score = self.game_board.board_list.count("white")

        self.player_scores["black"] = self.b_score
        self.player_scores["white"] = self.w_score

        self.score_blk.config(text="Black: " + str(self.player_scores["black"]))
        self.score_wht.config(text="White: " + str(self.player_scores["white"]))
        
    def save(self):
        """Saves the current game state to a file"""
        with open("save", "wb") as f:   
            pickle.dump(self.game_board.board_list, f)

    def load(self):
        """Loads the game state from a file"""
        with open("save", 'rb') as f:
            self.game_board.board_list = pickle.load(f)
        self.display_pawns()


if __name__ == "__main__":
    nb_players = 1; player_team="white"
    app = Interface(nb_players, player_team)
    app.mainloop()
