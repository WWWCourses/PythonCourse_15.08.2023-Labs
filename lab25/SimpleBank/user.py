class User:
	id = 1
	def __init__(self, name, email):
		self.name = name
		self.email = email
		self.id = User.id
		User.id+=1