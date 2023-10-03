### define Student class
class Student:
	# Class Attributes:
	count=0

	# Student constructor:
	def __init__(self, name, sn, age, score):
		print('Student constructor is called')
		print(self, name, sn, age, score)
		self.name = name
		self.surname = sn
		self.age = age
		self.score =score


	### instance attributes (properties)
	# 'name'
	# 'surname'
	# 'age'
	# 'score'
	### method:
	# change_age
	pass

pesho = Student('Petar', 'Petrov', 23, 5)
# pesho = Student()
# Student.__init__(pesho, 'Petar', 'Petrov', 23, 5)
# maria = Student('Maria', 'Marieva', 34, 4)

# print(pesho.name)
# print(maria.surname)







# print(pesho.name)
# print(maria.name)

# print( Student.count)
# # Student.count+=1
# pesho.count = 3
# print( pesho.count)
# print( maria.count)

# RAM:
# 	Student Class:
# 		count: 0

# 	pesho:
# 		count: 3

# 	maria:


## instance attributes:
# pesho.name = 'Petar'

# maria.name = 'Maria'
# print( pesho.name )
# # print( Student.name)
