import os
import tkinter as tk
import board

# Note
# on est oblige de manger un pion lorsque l'on joue (i.e. c'est a l'autre de jouer)

class Interface:
	def __init__(self):
		self.width, self.height = 600, 600 # canvas size
		self.game_board = board.Board()

		self.size_x = self.width//8
		self.size_y = self.height//8

		self.root = tk.Tk()
		self.root.title("Canvas Example")

		self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bg="#218543") 
		self.canvas.pack()

		self.canvas.bind("<Button-1>", self.on_click)

		self.display_grid()
		self.display_pawns()
		
		self.root.mainloop()

	def on_click(self, event):
		# get current position for array
		x, y = event.x//self.size_x, event.y//self.size_y 
		self.game_board.calculate(x,y)

		# x, y = x*self.size_x+ self.size_x//2, y*self.size_y+ self.size_y//2
		# self.canvas.create_oval(x-10, y-10, x+10, y+10, fill="blue")

		self.clear_canvas()
		self.display_grid()
		self.display_pawns()


	def clear_canvas(self):
		self.canvas.delete("all")
		self.display_grid()

	def display_pawns(self):
		# "radius" for the pawns
		pawn_size_x = self.size_x//2.5
		pawn_size_y = self.size_y//2.5
		# To place the pawns in the center of a box
		half_box_x = self.size_x//2
		half_box_y = self.size_y//2

		for i in range(8):
			for j in range(8):
				pawn = self.game_board.get(i,j)
				if pawn in (1,2):
					color = "white" if pawn == 1 else "black"
					self.canvas.create_oval(
						self.size_x*i-pawn_size_x + half_box_x, 
						self.size_y*j-pawn_size_y + half_box_y,
						self.size_x*i+pawn_size_x + half_box_x, 
						self.size_y*j+pawn_size_y + half_box_y,
						fill=color, outline=color)
				elif pawn == 3:
					# possible moves marker
					self.canvas.create_oval(
						self.size_x*i-pawn_size_x//2 + half_box_x, 
						self.size_y*j-pawn_size_y//2 + half_box_y,
						self.size_x*i+pawn_size_x//2 + half_box_x, 
						self.size_y*j+pawn_size_y//2 + half_box_y,
						fill="gray", outline="#218543")


	def display_grid(self):
		for i in range(8):
			if i != 0:
				tmp_x = self.size_x*i
				tmp_y = self.size_y*i
				self.canvas.create_line(tmp_x,0,tmp_x, self.height, width=3)
				self.canvas.create_line(0,tmp_y,self.width, tmp_y, width=3)


if __name__ == "__main__":
	app = Interface()

	if os.path.exists("temp.txt"):
		os.remove("temp.txt")