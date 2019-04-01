class Data_Manager:
	'''
	Class that will help in sorting the data used in the program, for example, 
	how to save the labirynth data or the blocks coordenates.
	'''
	def __init__(self, data):
		"""
		Data is the parameter that will pass the list or other data structure itself
		"""
		self.data = data


class Lab_Data_Manager(Data_Manager):
	
	def __init__(self, data):
		super(Lab_Data_Manager, self).__init__(data)

	def update_lab(self, rat_new_pos, rat_last_pos):
		"""
		A method that will update the lab data from where the RAT is and 
		from where he came from, in this case rat_last_pos.
		"""
		self.data[rat_new_pos] = 4
		self.data[rat_last_pos] = 5

	def get_lines(self):
		"""
		A method that will return the number of lines in the labirynth.
		"""
		return len(self.data)

	def get_columns(self):
		"""
		A method that will return the number of columns in the labirynth, 
		since each item from the data is a line, than the size of the item 
		will return us the number of columns.
		"""
		return len(self.data[1])

	def get_close_spaces(self, position_ref):
		"""
		- This method will return the spaces and "coordenates" from a position 
		given, the spaces will be given in a list as [up, right, down , left]

		- Position_ref must be a list that represents the x and y coordenates.
		"""
		x = position_ref[1]
		y = position_ref[0]
		close_spaces = [self.data[y - 1][x], self.data[y][x + 1], self.data[y + 1][x], self.data[y][x - 1]]
		return close_spaces

