import tkinter as tk
import pygame
import board
from interface import Interface


class Main_Interface:
	def __init__(self):
		self.root = tk.Tk()
		self.root.title("Othello")

		self.main_canvas = tk.Canvas(self.root, width= 500, height=500)
		self.main_canvas.pack()
		
        # Init pygame
		pygame.mixer.init()

		# Load musique
		pygame.mixer.music.load("Ressources/Airship_Thunderchild_opensource.mp3")
		# Play music continuously
		pygame.mixer.music.play(loops=-1)

        # Button for player vs player
		self.button_p_vs_p = tk.Button(self.main_canvas, text="Player vs Player", command=self.choose_color)
		self.button_p_vs_p.grid(row=0, column=0, pady=10)
		
        # Button for player vs AI
		self.button_p_vs_ai = tk.Button(self.main_canvas, text="Player vs AI", command=self.choose_color)
		self.button_p_vs_ai.grid(row=10, column=0, pady=10)
		
		# Checkbox for pausing or unpausing music 
		self.checkbox_var = tk.IntVar()
		self.checkbox = tk.Checkbutton(self.root, text="Stop music", variable=self.checkbox_var, command = self.play_stop_music)
		self.checkbox.pack(pady=5)
		

		self.root.mainloop()

	def play_stop_music(self):
		# Check if the checkbox is disable or not
		if self.checkbox_var.get() == 1:
			# Pause music
			pygame.mixer.music.pause()
		else :
			# Unpause music
			pygame.mixer.music.unpause()
			
	def choose_color(self):
		# Choose the color 
		# Note : The blacks begins
		self.root_choose = tk.Tk()
		self.root_choose.geometry("600x600")
		self.root_choose.title("Choose color")

		self.canvas_choose = tk.Canvas(self.root_choose, width=600, height=500)
		self.canvas_choose.grid(row=0, column=1, pady=1, padx=1)
		
		self.lab_choose = tk.Label(self.canvas_choose, text="Choose your team")
		self.lab_choose.grid(row=0, column=0, columnspan=2)
		
		self.image_b = tk.PhotoImage(master=self.root_choose, file="Ressources/black_p.png")
		self.image_w = tk.PhotoImage(master=self.root_choose, file="Ressources/white_p.png")
		

		self.button_black = tk.Button(self.root_choose,
            text="Black",
            image=self.image_b,
            compound=tk.LEFT,
            command=lambda: (Interface(2), self.root_choose.destroy())  # Close window after creating Interface
        )
		self.button_black.grid(row=1, column=0, padx=10)

		self.button_white = tk.Button(
            self.root_choose,
            text="White",
            image=self.image_w,
            compound=tk.LEFT,
            command=lambda: (Interface(2), self.root_choose.destroy())  # Close window after creating Interface
        )
		self.button_white.grid(row=1, column=1, padx=10)
		self.root_choose.mainloop()
if __name__ == "__main__":
	app = Main_Interface()