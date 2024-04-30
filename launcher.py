import tkinter as tk
from tkinter import *
from datetime import datetime
import interface as inter
import musik as mk
import os
import sys



class Main_Interface(Tk):
	def __init__(self, user=None):
		super().__init__()
		self.user = user
		self.geometry("700x500")
		self.title("Othello")
		self.minsize(width=700, height=500)
		self.maxsize(width=700, height=500)

		
		# Load images for the background and buttons
		self.image_main_menu = tk.PhotoImage(file="Ressources/images/main_menu_background.png")
		self.image_button_p = tk.PhotoImage(file="Ressources/images/button_icon_p_vs_p.png")
		self.image_button_ai = tk.PhotoImage(file="Ressources/images/button_icon_p_vs_ai.png")
		self.image_button_history = tk.PhotoImage(file="Ressources/images/button_icon_history.png")
		self.image_button_rules = tk.PhotoImage(file="Ressources/images/button_icon2_rules.png")
		
		# Main canvas setup
		self.main_canvas = tk.Label(self, width= 700, height=500, image=self.image_main_menu)
		self.main_canvas.grid()
		
        # Button for player vs player
		self.button_p_vs_p = tk.Button(self.main_canvas,width= 110, height=40,image=self.image_button_p, command=lambda:self.call_game(2,"black"))
		self.button_p_vs_p.place(x=60, y=140)
		
        # Button for player vs AI
		self.button_p_vs_ai = tk.Button(self.main_canvas,width= 110, height=40, image=self.image_button_ai, command=self.menu_choose_color)
		self.button_p_vs_ai.place(x=60, y=190)

		# Button for the game history
		self.button_history = tk.Button(self.main_canvas,width= 110, height=40, image=self.image_button_history, command=self.menu_history)
		self.button_history.place(x=60, y=240)
		
		# Button for the game rules
		self.button_rul = tk.Button(self.main_canvas,width= 110, height=40, image=self.image_button_rules, command=self.rules)
		self.button_rul.place(x=60, y=290)

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
		
		# Ensures proper exit
		self.protocol('WM_DELETE_WINDOW', self.exit_func)
	
		# Initial setup for color selection interface
		self.history()
		self.choose_color()
		self.mainloop()

	def menu_history(self):
		"""Hide the main canvas to display the team selection interface."""
		self.main_canvas.grid_forget()
		self.canvas_history.grid()

	def back_m_m(self):
		"""Return to the main menu."""
		self.canvas_history.grid_forget()
		self.main_canvas.grid()

	
	def menu_choose_color(self):
		"""Hide the main canvas to display the team selection interface."""
		self.main_canvas.grid_forget()
		self.canvas_choose.grid()

	def back_main_menu(self):
		"""Return to the main menu."""
		self.canvas_choose.grid_forget()
		self.main_canvas.grid()

	def rules(self):
		"""Navigate to the history or rules frame."""
		self.main_canvas.grid_forget()
		self.rules_frame.grid()


	def back(self):
		"""Return to the main menu from the rules frame."""
		self.rules_frame.grid_forget()
		self.main_canvas.grid()

	def history(self):
		"""
		Setting up a graphical interface to display a user's history. 
		"""
		# Create a frame to display the history with specified dimensions and background color
		self.canvas_history = tk.Frame(self, bg="#8FBC8F", width=700, height=500)

		# Create a Text widget inside the frame to display the history text
		self.text_history = tk.Text(self.canvas_history, wrap=tk.WORD, width=700, height=50)
		self.text_history.grid(row=1, column=1)

		# Open the file containing the history and read its content
		with open(os.path.join(sys.path[0], "history_game", self.user + ".txt"), "r") as f:   
			line_his = f.read()
			# Insert the history text into the Text widget
			self.text_history.insert(tk.END, line_his)

		# Configure the Text widget in read-only mode
		self.text_history.config(state=tk.DISABLED)

		# Create a vertical scrollbar to navigate through the text
		scrollbar = tk.Scrollbar(self.canvas_history, orient=tk.VERTICAL, command=self.text_history.yview)
		scrollbar.grid(row=1, column=2, sticky='ns')

		# Link the scrollbar to the Text widget
		self.text_history.config(yscrollcommand=scrollbar.set)

		# Create a button to go back to the previous page
		self.button_back3 = tk.Button(self.canvas_history, text="Previous page", command=self.back_m_m)
		self.button_back3.grid(row=0, column=0, pady=10)
	
	def choose_color(self):
		"""Setup for choosing the team color; default is 'black' starts the game."""
		self.canvas_choose = tk.Frame(self)

		self.lab_choose = tk.Label(self.canvas_choose, text="Choose your team")
		self.lab_choose.grid(row=0, column=0, columnspan=2, pady=50)
		
		# Load images
		self.image_b = tk.PhotoImage(master=self.canvas_choose, file="Ressources/images/black_p.png")
		self.image_w = tk.PhotoImage(master=self.canvas_choose, file="Ressources/images/white_p.png")

		self.button_black = tk.Button(self.canvas_choose, text="Black",  image=self.image_b, command=lambda:self.call_game(1,"black"),compound=tk.LEFT)
		self.button_black.grid(row=1, column=0, padx=10)

		self.button_white = tk.Button(self.canvas_choose, text="White", image=self.image_w, command=lambda:self.call_game(1,"white"), compound=tk.LEFT)
		self.button_white.grid(row=1, column=1, padx=10)
		
		self.button_back2 = tk.Button(self.canvas_choose, text="Previous page", command=self.back_main_menu)
		self.button_back2.grid(row=2, column=0, pady=10)

	def call_game(self, nb_players=2, player_team="black"):
		"""Initiate a game session."""
		self.exit_func()
		mk.music_player.swap_interface()
		inter.Interface(self.user,nb_players, player_team)
		
	def exit_func(self):
		"""Close the music player and the interface."""
		mk.music_player.destroy()
		self.destroy()


if __name__ == "__main__":
	app = Main_Interface()	