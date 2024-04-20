import tkinter as tk
from tkinter import *
from datetime import datetime
import interface as inter
import rule
import musik as mk



class Main_Interface(Tk):
	def __init__(self, user=None):
		super().__init__()
		self.user = user
		self.geometry("700x500")
		self.title("Othello")
		self.minsize(width=700, height=500)
		self.maxsize(width=700, height=500)

		self.image_main_menu = tk.PhotoImage(file="Ressources/images/main_menu_background.png")
		self.image_button_p = tk.PhotoImage(file="Ressources/images/button_icon_p_vs_p.png")
		self.image_button_ai = tk.PhotoImage(file="Ressources/images/button_icon_p_vs_ai.png")
		self.image_button_rules = tk.PhotoImage(file="Ressources/images/button_icon2_rules.png")
		
		self.main_canvas = tk.Label(self, width= 700, height=500, image=self.image_main_menu)
		self.main_canvas.grid()
		
        # Button for player vs player
		self.button_p_vs_p = tk.Button(self.main_canvas,width= 110, height=40,image=self.image_button_p, command=self.menu_choose_color)
		self.button_p_vs_p.place(x=60, y=140)
		
        # Button for player vs AI
		self.button_p_vs_ai = tk.Button(self.main_canvas,width= 110, height=40, image=self.image_button_ai, command=self.menu_choose_color)
		self.button_p_vs_ai.place(x=60, y=190)
		
		# Button for the game history
		self.button_historique = tk.Button(self.main_canvas,width= 110, height=40, image=self.image_button_rules, command=self.rules)
		self.button_historique.place(x=60, y=240)

		# Creating a new above the main canvas
		self.rules_frame = tk.Frame(self)
		self.lab = tk.Label(self.rules_frame, text="Ok")
		self.lab.grid()
		self.button_back = tk.Button(self.rules_frame, text="Page précédente", command=self.back)
		self.button_back.grid(row=2, column=0)
		
		
		# Checkbutton for stopping music
		self.check_button_var = tk.BooleanVar(value=(mk.music_player.music_on== False))
		self.check_button = tk.Checkbutton(self.main_canvas, text="Mute", variable=self.check_button_var, command=mk.music_player.switch_main)
		self.check_button.place(x=20, y=450)
		
		self.protocol('WM_DELETE_WINDOW', self.exit_func)
	
		self.choose_color()
		self.mainloop()

	
	def menu_choose_color(self):
		# Hide the main canvas to show the canvas where you can choose your team
		self.main_canvas.grid_forget()
		self.canvas_choose.grid()

	def back_main_menu(self):
		# Return to the main menu
		self.canvas_choose.grid_forget()
		self.main_canvas.grid()

	def rules(self):
		# Go to the history
		self.main_canvas.grid_forget()
		self.rules_frame.grid()


	def back(self):
		# Return to the main menu
		self.rules_frame.grid_forget()
		self.main_canvas.grid()
	
	def choose_color(self):
		# Choose the color 
		# Note : The blacks begins
		self.canvas_choose = tk.Frame(self)

		self.lab_choose = tk.Label(self.canvas_choose, text="Choose your team")
		self.lab_choose.grid(row=0, column=0, columnspan=2, pady=50)
		
		# Load images
		self.image_b = tk.PhotoImage(master=self.canvas_choose, file="Ressources/images/black_p.png")
		self.image_w = tk.PhotoImage(master=self.canvas_choose, file="Ressources/images/white_p.png")

		self.button_black = tk.Button(self.canvas_choose, text="Black",  image=self.image_b, command=self.call_game,compound=tk.LEFT)
		self.button_black.grid(row=1, column=0, padx=10)

		self.button_white = tk.Button(self.canvas_choose, text="White", image=self.image_w, command=self.call_game, compound=tk.LEFT)
		self.button_white.grid(row=1, column=1, padx=10)
		
		self.button_back2 = tk.Button(self.canvas_choose, text="Previous page", command=self.back_main_menu)
		self.button_back2.grid(row=2, column=0, pady=10)

	def call_game(self):
		self.exit_func()
		mk.music_player.swap_interface()
		inter.Interface(2)
		
	def exit_func(self):
		mk.music_player.destroy()
		self.destroy()


if __name__ == "__main__":
	app = Main_Interface()	