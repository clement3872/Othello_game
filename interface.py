import tkinter as tk
from tkinter import *
from tkinter import messagebox as tkm
import board
import launcher as minter
import musik as mk

# Définition de la classe Interface qui hérite de Tk de tkinter
class Interface(Tk):
    def __init__(self, nb_players, player_team="black"):
        super().__init__()

        # Initialisation des dimensions du canevas
        self.width, self.height = 600, 600 
        # Création de l'objet plateau de jeu
        self.game_board = board.Board(nb_players, player_team)
        # Définition des dimensions minimales et maximales de la fenêtre
        self.minsize(width=600, height=700)
        self.maxsize(width=600, height=700)

        # Calcul de la taille de chaque case du plateau
        self.size_x = self.width // 8
        self.size_y = self.height // 8
        # Initialisation des scores des joueurs
        self.player_scores = {"black": 2, "white": 2}

        # Configuration du titre de la fenêtre
        self.title("Plateau de l'Othello")

        # Création du canevas pour le jeu
        self.canvas = tk.Canvas(self, width=self.width, height=self.height, bg="#21854d")
        self.canvas.pack()

        # Association d'un événement de clic à une méthode
        self.canvas.bind("<Button-1>", self.on_click)
        
        # Création d'un bouton pour annuler le dernier coup joué
        self.redo_button = tk.Button(self, text="Undo", command=self.redo_move)
        self.redo_button.pack(side=tk.LEFT)

        # Affichage de l'équipe actuelle
        self.label_display = tk.Label(self, text=self.game_board.player_team)
        self.protocol('WM_DELETE_WINDOW', self.return_main)

        # Mise à jour et affichage initial du plateau
        self.game_board.update_with_possible_moves()
        self.display_grid()
        self.display_pawns()

        # Bouton pour quitter le jeu
        self.ret = tk.Button(self, text="Quit", command=self.return_main)
        self.ret.pack()

        # Option pour activer/désactiver la musique
        self.check_button_music = tk.BooleanVar(value=(mk.music_player.music_on == False))
        self.check_button_m = tk.Checkbutton(self, text="Mute", variable=self.check_button_music, command=mk.music_player.switch_board)
        self.check_button_m.place(x=500, y=650)

        # Affichage des scores des joueurs
        self.score_blk = tk.Label(self, text="Black: " + str(self.player_scores["black"]))
        self.score_wht = tk.Label(self, text="White: " + str(self.player_scores["white"]))
        self.score_blk.pack(side=tk.LEFT)
        self.score_wht.pack(side=tk.LEFT)

    # Méthode appelée lors de la fermeture de la fenêtre
    def return_main(self):
        self.exit_func()
        mk.music_player.swap_interface()
        minter.Main_Interface()

    # Méthode pour fermer la fenêtre
    def exit_func(self):
        self.destroy()

    # Gestion des événements de clic sur le canevas
    def on_click(self, event):
        x, y = event.x // self.size_x, event.y // self.size_y
        if self.game_board.get(x, y) == 0 or self.game_board.get(x, y) in ("white", "black"):
            print("You cannot play this move")
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

    # Méthode pour nettoyer le canevas
    def clear_canvas(self):
        self.canvas.delete("all")
        self.display_grid()

    # Affichage des pions sur le canevas
    def display_pawns(self):
        pawn_size_x = self.size_x // 2.5
        pawn_size_y = self.size_y // 2.5
        half_box_x = self.size_x // 2
        half_box_y = self.size_y // 2

        for i in range(8):  # colonnes
            for j in range(8):  # lignes
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
                    # Marqueur pour les coups possibles
                    self.canvas.create_oval(
                        self.size_x * i - pawn_size_x // 2 + half_box_x,
                        self.size_y * j - pawn_size_y // 2 + half_box_y,
                        self.size_x * i + pawn_size_x // 2 + half_box_x,
                        self.size_y * j + pawn_size_y // 2 + half_box_y,
                        fill="gray", outline="orange")

    # Affichage de la grille sur le canevas
    def display_grid(self):
        for i in range(1, 8):
            tmp_x = self.size_x * i
            tmp_y = self.size_y * i
            self.canvas.create_line(tmp_x, 0, tmp_x, self.height, width=3)
            self.canvas.create_line(0, tmp_y, self.width, tmp_y, width=3)

    # Vérification si le plateau est entièrement rempli
    def check_board_is_full(self):
        if self.game_board.board_is_full():
            if self.b_score > self.w_score:
                tkm.showinfo("The black wins")
            elif self.b_score < self.w_score:
                tkm.showinfo("The white wins")
            else:
                tkm.showinfo("Egalité")

    # Annulation du dernier mouvement
    def redo_move(self):
        if self.game_board.redo():
            self.clear_canvas()
            self.display_pawns()
            self.update_score()
        else:
            tkm.showinfo("No Moves to Redo", "There are no moves to redo.")

    # Mise à jour des scores
    def update_score(self):
        self.b_score = self.game_board.board_list.count("black")
        self.w_score = self.game_board.board_list.count("white")

        self.player_scores["black"] = self.b_score
        self.player_scores["white"] = self.w_score

        self.score_blk.config(text="Black: " + str(self.player_scores["black"]))
        self.score_wht.config(text="White: " + str(self.player_scores["white"]))

if __name__ == "__main__":
    nb_players = 2
    app = Interface(nb_players)
    app.mainloop()
