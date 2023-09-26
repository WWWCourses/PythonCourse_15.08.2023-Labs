# --------------------------------- Example 1 -------------------------------- #
# x = 1

# def foo(x):
# 	x=x+1
# 	print(f'x in foo: {x}')


# foo(2)
# print(f'x in global: {x}')

# OUTPUT:
# 	x in foo: 3
# 	x in global: 1

# RAM:
# 	0x1234: 0001 (1)
# 	0x3421: 00101010101010101 (<foo code>)
# 	0x8757: 0010 (3)

# global = {
# 	x:0x1234,
# 	foo: 0x3421
# }

# foo_local = {
# 	x:0x8757
# }

# --------------------------------- Example 2 -------------------------------- #
# x = 1

# def foo():
# 	# print(x) # UnboundLocalError
# 	# x = 2
# 	x=x+1 # UnboundLocalError
# 	# print(f'x in foo: {x}')

# foo()
# print(f'x in global: {x}')

# --------------------------------- Example 3 -------------------------------- #
# def foo(x):
# 	print(f'x in foo: {x}')

# 	def bar(x):
# 		x+=1
# 		print(f'x in bar: {x}')

# 	bar(3)


# x = 1
# foo(2)

# print(f'x in main: {x}')

# # OUTPUT:
# # x in foo: 2
# # x in bar: 4
# # x in main: 1


# --------------------------------- Example 4 -------------------------------- #
# def foo():
# 	print(f'x in foo: {x}')

# 	def bar():
# 		print(f'x in bar: {x}')

# 	bar()

# x = 1
# foo()
# print(f'x in global: {x}')

# OUTPUT:
# x in foo: 1
# x in bar: 1
# x in global: 1




