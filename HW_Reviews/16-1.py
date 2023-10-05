# Лекция 14 Наследяване задачи
# 1. Дефинирайте клас Human със свойства "собствено име" и "фамилно име".
# Дефинирайте клас Student, наследяващ Human, който има свойство "оценка".
# Дефинирайте клас Worker, наследяващ Human, със свойства "надница" и "изработени
# часове".

# Имплементирайте и метод "изчисли надница за 1 час", който смята колко
# получава работникът за 1 час работа, на базата на надницата и изработените часове.
# Напишете съответните конструктори и методи за достъп до полетата (свойства).
# A) направете списък от 10 студента
# Б) направете списък от 10 работника
# Вход:
# На първия ред на входа ще бъде подадено цяло число N, което ще представлява броя
# на редовете които трябва да бъдат прочетени. На всеки от следващите N реда ще бъде
# подадена информация за работник в следната последователност: Име Фамилия
# Надница
# 3
# Petar Dimitrov 16 91
# Nikolay Dimitrov 29 17
# Georgi Georgiev 17 23
# Изход:
# На изхода се очаква да се изпишат въведени работници и изчислената им надница.
# Примерен изход:
# Petar Dimitrov 0.1758241758241758241758241758
# Nikolay Dimitrov 1.7058823529411764705882352941
# Georgi Georgiev 0.739130434782608695652173913

class Human():
	def __init__(self, name, surname) -> None:
		self.name = name
		self.surname = surname

	def __str__(self) -> str:
		return f'{self.name}, {self.surname}'

class Student(Human):
	def __init__(self, name, surname, score ) -> None:
		super().__init__(name,surname)
		self.score = score

	def __str__(self) -> str:
		return super().__str__() + f' {self.score}'

class Worker(Human):
	def __init__(self, name, surname, wage, hours) -> None:
		super().__init__(name,surname)
		self.wage = wage
		self.hours = hours

	def __str__(self) -> str:
		return super().__str__() + f' {self.wage} per {self.hours}'

	def calc_pay_per_hour(self):
		return self.wage/self.hours



# student1 = Student('Ivan', 'Ivanov', 5)
# worker1 = Worker('Asen', 'Asenov', 100, 8)
# print(student1)
# print(worker1)
# print( worker1.calc_pay_per_hour())

students = [
	 Student('Ivan', 'Ivanov', 5),
	 Student('Ivan', 'Ivanov', 5),
	 Student('Ivan', 'Ivanov', 5),
	 Student('Ivan', 'Ivanov', 5),
	 Student('Ivan', 'Ivanov', 5),
	 Student('Ivan', 'Ivanov', 5),
	 Student('Ivan', 'Ivanov', 5),
	 Student('Ivan', 'Ivanov', 5),
	 Student('Ivan', 'Ivanov', 5)
]