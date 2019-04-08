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
		self.dp_location = []
		self.direction = "Right"
		self.step_counter = 0
		self.searching_bifurc = False
		self.steps_to_dest = 0

	def go_up(self):
		'''
		Moves the rat one position above.
		'''
		self.y = self.y - 1

	def go_right(self):
		'''
		Moves the rat one position right.
		'''
		self.x = self.x + 1

	def go_down(self):
		'''
		Moves the rat one position down.
		'''
		self.y = self.y + 1

	def go_left(self):
		'''
		Moves the rat one position left.
		'''
		self.x = self.x - 1

	def set_bifurcation(self, look, around):
		'''
		Method that will see the avaible paths for the rat
		look is a tuple that will show where to look for up/down = (0,2) or right/left = (1,3)
		'''

		if around[look[0]] != 1 and around[look[1]] == 1:
			possibilities = (True, False) 
		
		elif around[look[0]] == 1 and around[look[1]] != 1:
			possibilities = (False,True)  
		
		elif around[look[0]] != 1 and around[look[1]] !=1:
			possibilities = (True, True)
		
		else:
			possibilities = (False, False) 

		return possibilities

	def go_to_bifurc(self, options):
		
		destination = self.dp_location.pop()
		step = destination[0]
		d_to_d = destination[1]
		self.steps_to_dest = self.step_counter - step
		direction = 0 if d_to_d == 2 else 1 if d_to_d == 3 else 2 if d_to_d == 0 else 3
		return options[direction]

	def make_decision(self, bifurc, options, dir_as_num, around, check = False, know_all = False):
		
		if bifurc == (False, False) or know_all == True:
			self.searching_bifurc = True
			return self.go_to_bifurc(options)

		elif check == True:

			if around.count(2) != 0:
				print('Hell yeah!')
				dir_as_num = around.index(2)
			else:
				dir_as_num = around.index(0)
			
			return options[dir_as_num]

		elif bifurc == (True, True):
			
			dir_as_num -= 1
			return  options[dir_as_num]

		else:
			if dir_as_num == 0 or dir_as_num == 2:
				if bifurc[0] == True:
					dir_as_num = 1
				else:
					dir_as_num = 3

			else:
				if bifurc[0] == True:
					dir_as_num = 0
				else:
					dir_as_num = 2


			return options[dir_as_num]


	def walk(self, around):
		'''
		This method is reponsible for the rat moviment.
		It receives a list of the spaces close to it by one positon up, right, down and left.
		The logic is this: the rat will follow a direction untill it hits
		a wall. If it hits a wall it will look the the other direction
		for example: It walks all the way to the right, it finds a wall then it will
		look up and down.
		In case it finds a dead end it will go know_all from where he came from and search for 
		places he went straight but had an entrance.
		'''

		moviments = {"Up": self.go_up,
						"Right": self.go_right,
						"Down": self.go_down,
						"Left": self.go_left}
		options = list(moviments.keys())
		# It will check if the bifurcations are avaible, right/left or up/down
		bifurc = (False, False)
		
		# Direction as number. This will give us the position in the list of the direction
		dir_as_num = options.index(self.direction) 
		bifurc = self.set_bifurcation((1,3), around) if dir_as_num %2 == 0 else self.set_bifurcation((0,2), around)

		if self.searching_bifurc == True:
			self.steps_to_dest -= 1
			if self.steps_to_dest == 0:
				
				self.searching_bifurc = False

				if around.count(0) == 0 and around.count(2) == 0:
					self.direction = self.make_decision(bifurc, options, dir_as_num, around, know_all = True)
				else:
					self.direction = self.make_decision(bifurc, options, dir_as_num, around, check = True)

		# this if statement will tell if the rat found a wall in its straight walk.
		elif around[dir_as_num] not in [0,2,4]:
			self.direction = self.make_decision(bifurc, options, dir_as_num, around)

		# Adding the correct bifurcations
		if bifurc != (False,False) and around.count(0) != 0 or around.count(2) != 0:
			dir_as_num = options.index(self.direction) # getting the new dir_as_num position
			self.dp_location.append((self.step_counter, dir_as_num))

		moviments[self.direction]()
		self.position = [self.y, self.x]
		self.step_counter = self.step_counter + 1 if self.searching_bifurc != True else self.step_counter - 1
		

