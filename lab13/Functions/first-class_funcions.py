# --------------------------------- Example 1 -------------------------------- #
# def foo():
# 	print('foo')
# 	return 5

# bar = foo
# foo = 5

# print( bar ) # function

# # print( foo() )
# print( bar() )


# --------------------------------- Example 2 -------------------------------- #

def foo(f):
	# f = bar
	print('foo' * 10)
	print( f() )

def bar():
	print('Bar')
	return 1


def baz():
	print('Baz')
	return 2

foo(f=bar)
foo(baz)



# OUTPUT:
# foo
# Bar


