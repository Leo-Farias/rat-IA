from tkinter import *

class Viewer():
	'''
	This class will be responsible for showing the labirynth and where the rat is moving,
	it uses the tkinter library for the interface.
	'''
	def __init__(self, canvas_bg = "#b5c0d1"):
		self.WINDOW_HEIGHT = 550
		self.WINDOW_WIDTH = 550
		self.window = Tk()
		self.canvas = Canvas(self.window, height = self.WINDOW_HEIGHT, width = self.WINDOW_WIDTH, bg = canvas_bg)

	def config_basic(self, t = "Rat Labirynth"):
		'''
		Method that will config the basic values for our window window
		'''
		self.window.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")
		self.window.title = t 
		self.window.resizable(False, False)

class Artist():
	'''
	This class will be responsible for drawing the shapes in our canvas, such as painting the
	blocks that will represent where the rat is.
	'''
	def __init__(self, window, drawing_space):
		
		self.window = window
		self.drawing_space = drawing_space
		self.first_point_X = 25 # This is where the artist will start drawing in X
		self.first_point_Y = 30 # This is where the artist will start drawing in Y

	def draw_labirynth(self, lab_data):
		'''
		This method is responsible for showing the labyrinth based on the data passed, such as
		if the block is a wall or empty space.
		'''
		size = 20
		move = 25
		point_X = self.first_point_X
		point_Y = self.first_point_Y
		outline_color = "#262626"
		block_color = {0:'#efefef', 1: "#444444", 2: "#ad4e4e", 3: "#547a76", 4: "#a5bdc6"}
		# 0 = Empty Space    1 = Wall   2 = Finish Line   3 = Rat    4 = Space walked by the rat

		# Creating our blocks with for loops.
		# Each item from lab_data corresponds to a line list, and each item from that line list
		# is a column
		for line in lab_data:			
			for column in line:
				
				self.drawing_space.create_rectangle(point_X, point_Y, point_X + size, point_Y + size, width = 2, outline = outline_color, fill = block_color[column])
				point_X += move

			point_X = self.first_point_X
			point_Y += move

		self.drawing_space.pack()
		self.window.mainloop()
