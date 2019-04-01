from time import sleep

class Board:
	
	def __init__(self, height, width, walls):
		self.height = height
		self.width = width
		self.walls = walls
		self.final_form = []

	def setup_lab(self):

		for lines in range(0, self.height):
			for columns in range(0, self.width):
				self.final_form.append(0)

		for wall_pos in self.walls:
			self.final_form[wall_pos] = 1

	def give_close_spaces(self, reference_pos):
		close_spaces = []
		where_to_look = [self.width + reference_pos, - self.width + reference_pos, 1 + reference_pos, -1 + reference_pos]
		counter = 0
		print(where_to_look)
		while counter < len(where_to_look):
			try:
				# UP space
				close_spaces.append(self.final_form[where_to_look[counter]])
				print(self.final_form[where_to_look[counter]])
			except:
				close_spaces.append("Out of Bounds")
			counter += 1
		
		print(close_spaces)
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
			
			if space == 0:
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
			self.board.final_form[self.rat.last_position] = 0
			self.board.final_form[self.rat.position] = 'R'
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
			counter +=1



if __name__ == "__main__":

	my_board = Board(9,10,[2,20,38,45,82])
	my_board.setup_lab()
	my_rat = Rat(my_board.width)
	my_displayer = Displayer(my_board, my_rat)
	my_displayer.display_board()