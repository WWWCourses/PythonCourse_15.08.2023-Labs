### define Student class
class Student:
	# Class Attributes:
	count=0

	# Student constructor:
	def __init__(self, name, sn, age, score):
		self.name = name
		self.surname = sn
		self.age = age
		self.score =score
		Student.count=Student.count+1


students = [
	Student('Petar', 'Petrov', 23, 5),
	Student('Maria', 'Marieva', 34, 4),
	Student('Asen', 'Asenov', 34, 6),
]

hier_score_student = sorted(students,key=lambda student:student.score,reverse=True)[0]

print( hier_score_student.name )
print( Student.count)

