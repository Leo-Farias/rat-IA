class Checker():

	def write_value(self, value_to_write, file_path):
		'''
		Method that writes a value to a file.
		'''
		doc = open(file_path + ".txt", 'w')
		doc.write(str(value_to_write))
		doc.close()

	def get_value(self, file_path):
		'''
		Method that gets all the written text in a file.
		'''
		try:
			doc =  open(file_path + ".txt", 'r')
			result = doc.read()
			doc.close()
			return result
		
		except:
			return None
 

	def check_value(self, value_to_check, file_path):
		'''
		Method that checks a value from the text inside a file.
		'''

		file_path += ".txt"
		value_to_check = str(value_to_check)

		try:
			doc = open(file_path, "r+")
			value_from_doc = doc.read()
			doc.close()
			return value_from_doc == value_to_check

		except:
			return False

		

