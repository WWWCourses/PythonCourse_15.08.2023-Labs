
class Car():
	def __init__(self, model, speed) -> None:
		self.model = model
		self.speed = speed

	def __str__(self):
		return f'model-{self.model}, speed-{self.speed}'

	def __lt__(self, other):
		return self.speed<other.speed

	def drive(self):
		print(f'{self.model} is driving with {self.speed}')

car1 = Car('Ford', 400)
car2 = Car('BMV', 350)

# car_dict = {
# 	'model': 'Ford',
# 	'speed': 300
# }

# print(car_dict)
# print(car1)
# print(car2)

# print(car1.__dir__())
# print(dir(car1))
print(car1<car2)