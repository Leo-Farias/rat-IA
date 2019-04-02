class Rat:
	'''
	The rat class is pretty much the main class, it's mission is to find the exit
	He wont receive the labyrinth list because that would be cheating
	istead he will have to choose it's moviment based on what it can see
	'''

	def __init__(self, x, y):
		
		self.x = x
		self.y = y
		self.position = [self.x, self.y]
		self.last_position = []

	def update_coordenates(self, x, y):
		self.x = x
		self.y = y

	def walk(self, around):
		choice = "default"
		moviments = {"Up": [self.y - 1, self.x],
						"Right": [self.y, self.x + 1],
						"Down": [self.y + 1, self.x],
						"Left": [self.y, self.x - 1]}
		options = ["Up", "Right", "Down", "Left"]
		counter = 0
		change_direction = False
		
		for space in around:
			

		#If the choice remains as "default" than it means that the rat found a dead end.

		self.position = moviments[choice]
		self.update_coordenates(self.position[1], self.position[0])	
