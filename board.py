import subprocess
# import os 

class Board(object):
	"""
	0 = empty
	1 = white pawn
	2 = black pawn
	3 = possible moves 
	"""

	def __init__(self):

		self.board_list = [
			0, 0, 0, 0, 0, 0, 0, 0,
			0, 0, 0, 0, 0, 0, 0, 0,
			0, 0, 0, 0, 0, 0, 0, 0,
			0, 0, 0, 1, 2, 0, 0, 0,
			0, 0, 0, 2, 1, 0, 0, 0,
			0, 0, 0, 0, 0, 0, 0, 0,
			0, 0, 0, 0, 0, 0, 0, 0,
			0, 0, 0, 0, 0, 0, 0, 0
		]
		subprocess.call(["gcc", "processing.c", "-o", "a.out"]) # compiling C file, output: a.out

	def get(self, row, col):
		return self.board_list[row*8 + col]

	def calculate(self,i,j):

		# write board in file `temp.txt` - C file will read it
		# `context.txt` contains i,j and board_list, one number per line
		with open("temp.txt", "w") as file:
			file.write(f"{i}\n{j}\n")
			for el in self.board_list:
				file.write(str(el)+"\n")

		print("Calculating...")

		# output = subprocess.call("./a.out") # running compiled C file
		output = subprocess.call(["./a.out", "calculate"]) # running compiled C file
		if output == 1:
			print("ERROR: something went wrong in the `Baord.calculate`")
			return 1

		print("Done calculating.")


# to test
if __name__ == '__main__':
	b = Board()
	b.calculate(0,0)
