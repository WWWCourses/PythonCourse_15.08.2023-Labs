from matplotlib.pyplot import cla

class C(object):
	def __init__(self) -> None:
		print('C constructor')

	def foo(self):
		print('foo in c: ', self.id)

class B:
	def __init__(self) -> None:
		self.name = 'B'
		print('C constructor')

	def bar(self):
		print('bar in B: ', self.id)

class A(B, C):
	def __init__(self, id) -> None:
		super().__init__()
		# super(B,self).__init__()
		# B.__init__(self)
		# C.__init__(self)
		self.id=id
		print('A constructor', self)


if __name__=='__main__':
	a1=A(1) # instatiate class A into a (A.__init__(a1, 1))
	a2=A(2) # instatiate class A into a

	print(a1.id) #/1
	print(a1.name)

	a1.foo() # C.foo(a1)
	a1.bar() # B.bar(a1)




