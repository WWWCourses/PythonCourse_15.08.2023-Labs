class Animal:
	def __init__(self,name,age=1) -> None:
		print('Animal Constructor is called')
		self.name = name
		self.age = age
		self.foo = 1

	def make_sound(self,sound):
		print(f'{self.name} which is {self.age} say: {sound}')

class Dog(Animal):
	def __init__(self,name,age) -> None:
		super().__init__(name,age)


class Cat(Animal):
	def __init__(self,name,age) -> None:
		# self.name = name
		super().__init__(name,age)
		self.life_count = 9

	def make_sound(self, sound):
		super().make_sound(sound)
		print(f'current lives: {self.life_count}')

	def decrease_life(self):
		self.life_count-=1
		print(f'lives left: {self.life_count}')

dog1 = Dog('Dog1',12)
cat1 = Cat('Cat1',5)
animal1 = Animal('Lion1')

print( dog1.foo)

# dog1.make_sound('bau bau')
# cat1.make_sound('miao miao')






