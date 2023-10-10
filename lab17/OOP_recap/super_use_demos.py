# -------------------------- Simple (Syntax) Example ------------------------- #
# class A:
# 	def m1(self):
# 		print('m1 in A is called')

# class B:
# 	def m1(self):
# 		print('m1 in B is called')

# class C(B):
# 	def m2(self):
# 		print('m2 in C is called')
# 		### call m1 from A:
# 		## Variant 1:
# 		# A.m1(self)

# 		## Variant 2 (with super())
# 		super().m1()


# c = C()
# c.m2()

# --------------------------------- Example 2 -------------------------------- #
# class Automobile:
# 	def __init__(self, model, speed) -> None:
# 		self.model = model
# 		self.speed = speed

# 	def drive(self):
# 		print(f'{self.model} is driving with {self.speed}')


# class Motorcycle:
# 	def __init__(self,model, speed) -> None:
# 		self.model = model
# 		self.speed = speed

# 	def drive(self):
# 		print(f'{self.model} is ... with {self.speed}')

# class Car(Automobile):
# 	def __init__(self, model, speed, seats):
# 		self.seats = seats
# 		# Automobile.__init__(self,model, speed)
# 		super().__init__(model, speed)

# 		# Automobile.drive(self)
# 		super().drive()


# ford = Car('Ford', 300, seats=5)
# print(ford.seats)
# # Automobile.__init__(ford, 'Ford', 300, seats=5)
# harley = Motorcycle('Harley Davidson', 280)

# ford.drive()
# harley.drive()

# --------------------------- Example 3 (advanced) --------------------------- #
# class A:
# 	def m1(self):
# 		print('m1 in A is called')

# class B:
# 	def m1(self):
# 		print('m1 in B is called')

# class C(A,B):
# 	def m2(self):
# 		print('m2 in C is called')

# 		# A.m1(self)
# 		# super().m1()

# 		B.m1(self)
# 		super(A,self).m1()


# c = C()
# c.m2()