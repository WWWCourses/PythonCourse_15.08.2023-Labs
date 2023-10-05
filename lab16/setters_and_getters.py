class Dog:
	def __init__(self, name) -> None:
		self.__name = name

	@property
	def name(self):
		print('name getter')
		return self.__name

	@name.setter
	def name(self, new_name):
		print('name setter')
		self.__name = new_name


dog1 = Dog('Dog1')
dog2 = Dog('Dog2')




print(dog1.name)
dog1.name = 'Sharo'
print(dog1.name)

# print(dir(dog1))




