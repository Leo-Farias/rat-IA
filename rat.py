from time import sleep
from os import system

class Space:
	'''
	Class that populates our board, each space can have or have not a wall and the rat might or might not be on it.
	'''
	def __init__(self, wall, rat = False):
		self.wall = wall
		self.rat = rat
	
	def turn_wall(self):
		'''
		INFO: Method that turns the space's wall paremeter true.
		'''
		self.wall = True

	def __str__ (self):
		'''
		INFO: Rewrite the string method so when the displayer class prints out the spaces it's more legible.
		'''
		
		if self.wall == True:
			return '*'

		elif self.rat == True:
			return 'R'

		else:
			return '0'


class Board:
	'''
	Class that stores the spaces. It also gives the rat information about where it is, such as the 
	'give_close_spaces' method.
	'''
	
	def __init__(self, height, width, walls):
		self.height = height
		self.width = width
		self.walls = walls
		self.final_form = []

	def setup_lab(self):
		'''
		INFO: This method populates the final_form paremeter with the spaces beeing the itens of the list.
		'''
		for lines in range(0, self.height):
			for columns in range(0, self.width):
				# this if statment is getting all the border positions and setting it to be walls.
				if columns == 0 or columns == self.height or lines == 0 or lines == self.height -1:
					space = Space(True)
				else:
					space = Space(False)
				self.final_form.append(space)

		for wall_pos in self.walls:
			self.final_form[wall_pos].turn_wall()

	def give_close_spaces(self, reference_pos):
		'''
		INFO: This method is responsible for sending a list for the rat class which based on it the rat can "see" if there
		are any walls around it. 
		INPUT: The method needs a reference position.
		OUTPUT: It returns a list with Space objects.
		'''
		close_spaces = []
		where_to_look = [- self.width + reference_pos, 1 + reference_pos, self.width + reference_pos, -1 + reference_pos]
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

	def __init__(self, columns, start_at):
		self.map = []
		self.columns = columns
		self.position = start_at
		self.moviments = {'Up': -self.columns, 'Right': 1, 'Down': self.columns,  'Left': -1}
		self.last_position = 0
		self.moves_made = []

	def choose_moviment(self, around):
		counter = 0
		directions = ['Up', 'Right', 'Down', 'Left']
		for space in around:
			print(space.wall)
			print(counter)
			print(self.position)
			
			if space.wall == False:
				return directions[counter]
			counter += 1	

	def walk(self, around):
		self.last_position = self.position
		move_chosen = self.choose_moviment(around)
		self.position += self.moviments[move_chosen]
		self.moves_made.append(move_chosen)

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
			last_space = False
			self.board.final_form[self.rat.position] = Space(False, rat = True)
			while break_line < self.board.width and last_space != True:

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
					last_space = True
				
				else:
					position +=1

			sleep(1)
			system('clear')
			self.start_run()
			self.board.final_form[self.rat.last_position] = Space(False)
			counter +=1



if __name__ == "__main__":

	my_board = Board(9,10,[21,22,23,15,25,35,45,44,43])
	my_board.setup_lab()
	my_rat = Rat(my_board.width, 11)
	my_displayer = Displayer(my_board, my_rat)
	my_displayer.display_board()
	print(my_rat.moves_made)