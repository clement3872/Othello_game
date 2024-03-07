import subprocess
# import os 

class Board(object):
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

	def get(self, row, col):
		return self.board_list[row*8 + col]

	def calculate(self,i,j):
		subprocess.call(["gcc", "test.c"]) 
		print("Calculating")
		output = subprocess.call("./a.out")
		if output == 1: print("FATAL ERROR: something went wrong in the `Baord.calculate`")

		print("done")

if __name__ == '__main__':
	b = Board()
	b.calculate()

