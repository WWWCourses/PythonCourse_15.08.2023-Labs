class A:
	a = 1
	def m(self):
		print('m in A')

class B:
	a = 2
	def m(self):
		print('m in B')

class C(A,B):
	def m(self):
		# A.m(self)
		# B.m(self)
		super().m()
		super(A,self).m()

c = C()
print(c.a)
# print(C.mro())
# print(c.a)
c.m()

