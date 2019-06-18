import DataManager
import Interface
import Actioner
import Checker
from time import sleep

# SAVING THE SPACES IN A LIST
# EACH ITEM OF THE LIST REPRESENTS A LINE, 
# AND EACH ITEM FROM THOSE LISTS REPRESENTS THE COLUMNS
# 0 = Empty Space
# 1 = Wall 
# 2 = Finish Line
# 3 = Rat 
# 4 = Space walked by the rat

labyrinth = [
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
	[1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 2, 0, 1],
	[1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
	[1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
	[1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
	[1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
	[1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
	[1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
	[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1],
	[1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
	[1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
	[1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
	[1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
	[1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
	[1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
	[1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Creating our objects
pandin = DataManager.Data_Manager(labyrinth)

interface = Interface.Viewer()
interface.config_basic() #setting window size values

da_vinci = Interface.Artist(interface.window, interface.canvas)

mickey = Actioner.Rat(1,1)

machado = Checker.Checker()

following_correct_path = machado.check_value(labyrinth, "files/last_lab")

machado.write_value(labyrinth, "files/last_lab")

while True:

	#Showing the pandin
	da_vinci.draw(pandin.data)

	#Saving last position as 4, spaces already walked by the rat
	pandin.data[mickey.y][mickey.x] = 4

	if not following_correct_path:

		# Rat chooses it's moviment.
		mickey.walk(pandin.get_close_spaces(mickey.position))
		
		# If statement for end game
		if pandin.data[mickey.y][mickey.x] == 2:
			print('Finished.')
			machado.write_value(mickey.correct_path, 'files/correct_path')
			break #if the game finished then it will break the loop
		else:
			#updating the rat position in the lab data.
			pandin.data[mickey.y][mickey.x] = 3

	else:

		# We only update the first time.
		if len(mickey.correct_path) == 0:
			mickey.correct_path = machado.get_value('files/correct_path').split()
		mickey.follow_path()

		if len(mickey.correct_path) == 0:
			print('Finished')
			break

		else:
			pandin.data[mickey.y][mickey.x] = 3

	sleep(0.01)
	
	#clearing the vieweer for new draw
	da_vinci.clear_painting()