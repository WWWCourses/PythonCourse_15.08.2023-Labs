# Задача 2. Декларирайте конструктор за класа Student, които да инициализира всички
# атрибути на класа. Данните за полетата, които не са известни трябва да се
# инициализират съответно със стойности с None, 0, или “”.

class Student:
	def __init__(self, name="", course=None, univercity="", mail="", tel=0) -> None:
		self.name = name
		self.course = course
		self.univercity = univercity
		self.mail = mail
		self.tel = tel



std1 = Student('Petar', 'Programming',)
std2 = Student('Asen', 'Math')
