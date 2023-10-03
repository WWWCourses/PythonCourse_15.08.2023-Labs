class A:
	# class attribute:
	x = 99

	# def __init__(self, x) -> None:
	# 	# instance (member) attributes
	# 	self.x = x



# a1 = A(3)

a1 = A()
a1.x = 3
# a1.foo = lambda x:x+1

print( a1.foo(1) )



# print(a1.x)
# print(A.x)