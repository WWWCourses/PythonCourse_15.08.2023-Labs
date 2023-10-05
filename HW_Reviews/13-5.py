# Задача 5. Модифицирайте текущия код на класа Student така, че да капсулирате данните в класа чрез свойства


class Student:
	def __init__(self, name="", course=None, univercity="", mail="", tel=0) -> None:
		self._name = name
		self._course = course
		self._univercity = univercity
		self._mail = mail
		self._tel = tel

	@property
	def tel(self):
		return self._tel

	@tel.setter
	def tel(self, new_tel):
		self._tel = new_tel

std1 = Student('Petar', 'Programming',)
std2 = Student('Asen', 'Math')


std1.tel = 1234
std1.name  = "Pesho"
print(std1.tel)