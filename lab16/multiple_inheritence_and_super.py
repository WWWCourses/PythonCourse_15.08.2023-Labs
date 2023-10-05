class A:
	def __init__(self):
		print("In A")

class B(A):
	# def __init__(self):
	# 	print("In B")
		# super().m()
	pass

class C(A):
	def __init__(self):
		print("In C")
		# super().m()

class D(B, C):
	def __init__(self):
		print("In D")
		super(B,self).__init__()
		super().__init__()


d = D()
# d.m()
# b = B()
print(D.mro())
