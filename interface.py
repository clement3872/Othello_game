import tkinter as tk
import board

# Note
# on est oblige de manger un pion lorsque l'on joue (i.e. c'est a l'autre de jouer)

class Interface:
	def __init__(self):
		self.width, self.height = 400, 400 # canvas size
		self.game_board = board.Board()

		self.root = tk.Tk()
		self.root.title("Canvas Example")

		self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bg="#218543") 
		self.canvas.pack()

		self.canvas.bind("<Button-1>", self.place_pawn)

		self.clear_button = tk.Button(self.root, text="Clear Canvas", command=self.clear_canvas)
		self.clear_button.pack()

		self.display_grid()
		
		self.root.mainloop()

	def place_pawn(self, event):
		size_x = self.width//8
		size_y = self.height//8

		x, y = event.x//size_x, event.y//size_y # get current position
		x, y = x*size_x+ size_x//2, y*size_y+ size_y//2

		self.canvas.create_oval(x-10, y-10, x+10, y+10, fill="blue")

	def clear_canvas(self):
		self.canvas.delete("all")
		self.display_grid()

	def display_grid(self):
		size_x = self.width//8
		size_y = self.height//8

		for i in range(8):
			if i != 0:
				tmp_x = size_x*i
				tmp_y = size_y*i
				self.canvas.create_line(tmp_x,0,tmp_x, self.height, width=3)
				self.canvas.create_line(0,tmp_y,self.width, tmp_y, width=3)


if __name__ == "__main__":
	app = Interface()