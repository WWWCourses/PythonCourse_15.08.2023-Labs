class A:
	# class method:
	def class_method(x):
		print(f'x in class_method: {x}')

	def __init__(self, x) -> None:
		self.x = x

	# instance method:
	def instance_method(self, x):
		print(f'self in instance_method: {self}')
		print(f'x in instance_method: {x}')


	def increment_x(self):
		self.x = self.x + 1


	def setX(self,new_x):
		self.x = new_x

	def getX(self):
		return self.x

a1 = A(1)
a2 = A(2)

# A.class_method(1)
# a1.instance_method(1)
# # A.instance_method(a1, 1)


print(a1.x) # 1
print(a2.x) # 2

a1.increment_x()
a2.increment_x()

# a1.x = 100000
a1.setX(10000)

# print(a1.x)
print( a1.getX() )







