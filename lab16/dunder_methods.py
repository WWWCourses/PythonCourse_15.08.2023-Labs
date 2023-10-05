# __str__ method
class Student:
	# Student constructor:
	def __init__(self, name, sn, age, score):
		self.name = name
		self.surname = sn
		self.age = age
		self.score =score
	def __str__(self) -> str:
		# print('___Str___ is called')
		return f"name:{self.name}, surname:{self.surname}"



std1 = Student('Petar', 'Petrov', 23, 5)
std2 = Student('Maria', 'Marieva', 34, 4)
std3 = Student('Asen', 'Asenov', 34, 6)

print(std1)
print(std2)