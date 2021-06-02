import os, json
class DataStore:
	
	directory = r'C:\Users\parvi\OneDrive\Desktop'
	file_name = 'Sample.txt'
	full_path = os.path.join(directory, file_name)
	
	def __init__(self, file_path=full_path):
		
		self.file_path = file_path
		
		# create the file if it doesn't exist
		open(self.file_path, 'a').close()
	
	def create(self, key, value):
		
		# Bring text_file into memory and convert it to dictionary
		with open(self.file_path, 'r') as f:
			text_file = f.read()
		self.text_file_as_dict = {}
		if text_file != "":
			self.text_file_as_dict = json.loads(text_file)
		
		# Make necessary changes
		self.text_file_as_dict[key] = json.loads(value)
		
		# Write changes back into the text_file
		with open(self.file_path, 'w') as f:
			f.write(json.dumps(self.text_file_as_dict, indent=4))
	
	def read(self, key):
		
		# Bring text_file into memory and convert it to dictionary
		with open(self.file_path, 'r') as f:
			text_file = f.read()
		self.text_file_as_dict = json.loads(text_file)
		
		# Return specified value
		if key in self.text_file_as_dict:
			return json.dumps(self.text_file_as_dict[key], indent=4)
		else:
			return "Key doesn't exist"
	
	def delete(self, key):
		
		# Bring text_file into memory and convert it to dictionary
		with open(self.file_path, 'r') as f:
			text_file = f.read()
		self.text_file_as_dict = json.loads(text_file)
		
		# Make necessary changes
		if key in self.text_file_as_dict:
			del self.text_file_as_dict[key]
		else:
			return "Key doesn't exist"
		
		# Write changes back into the text_file
		# This will be executed only if the key is found and deleted
		with open(self.file_path, 'w') as f:
			f.write(json.dumps(self.text_file_as_dict, indent=4))

