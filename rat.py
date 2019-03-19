from time import sleep
from os import system

class Space:
	def __init__(self, border, wall, rat = False):
		self.border = border
		self.wall = wall
		self.rat = rat
	
	def turn_wall(self):
		self.wall = True

	def __str__ (self):
		
		if self.wall == True:
			return '1'

		elif self.rat == True:
			return 'R'

		else:
			return '0'


class Board:
	
	def __init__(self, height, width, walls):
		self.height = height
		self.width = width
		self.walls = walls
		self.final_form = []

	def setup_lab(self):

		for lines in range(0, self.height):
			for columns in range(0, self.width):
				if columns == 0 or columns == self.height or lines == 0 or lines == self.height -1:
					space = Space(True, False)
				else:
					space = Space(False, False)
				self.final_form.append(space)

		for wall_pos in self.walls:
			self.final_form[wall_pos].turn_wall()

	def give_close_spaces(self, reference_pos):
		close_spaces = []
		where_to_look = [self.width + reference_pos, - self.width + reference_pos, 1 + reference_pos, -1 + reference_pos]
		counter = 0
		while counter < len(where_to_look):
			try:
				# UP space
				close_spaces.append(self.final_form[where_to_look[counter]])
			except:
				close_spaces.append("Out of Bounds")
			counter += 1
		return close_spaces

class Rat:

	def __init__(self, columns):
		self.map = []
		self.columns = columns
		self.position = 0
		self.moviments = {'Up': self.columns, 'Down': - self.columns, 'Right': 1, 'Left': -1}
		self.last_position = 0

	def choose_moviment(self, around):
		counter = 0
		for space in around:
			
			if space.wall == False:
				return 'Up' if counter == 0 else 'Down' if counter == 1 else 'Right' if counter == 2 else 'Left'
			counter += 1	

	def walk(self, around):
		self.last_position = self.position
		self.position += self.moviments[self.choose_moviment(around)]

class Displayer:

	def __init__(self, board, rat):
		self.board = board
		self.rat = rat

	def start_run(self):
		self.rat.walk(self.board.give_close_spaces(self.rat.position))

	def display_board(self):
		counter = 0
		while counter < 30:
			break_line = 0
			position = 0
			last_position = False
			self.board.final_form[self.rat.last_position] = Space(False, False)
			self.board.final_form[self.rat.position] = Space(False, False, rat = True)
			while break_line < self.board.width and last_position != True:

				if break_line == 0:
					print(f"| {self.board.final_form[position]} | ", end = '')
					break_line += 1

				elif break_line != self.board.width -1:
					print(f"{self.board.final_form[position]} | ", end = '')
					break_line += 1
				
				else :
					print(f"{self.board.final_form[position]} |")
					break_line = 0

				if position == len(self.board.final_form) - 1:
					last_position = True
				
				else:
					position +=1

			sleep(0.5)
			self.start_run()
			system('cls')
			counter +=1



if __name__ == "__main__":

	my_board = Board(9,10,[2,10,80,20,38,45,82])
	my_board.setup_lab()
	my_rat = Rat(my_board.width)
	my_displayer = Displayer(my_board, my_rat)
	my_displayer.display_board()