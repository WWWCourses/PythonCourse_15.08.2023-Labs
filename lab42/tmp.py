def slot():
	print('hi')


def connect(f):
	# f = None
	print('connect will call slot....')
	f()


connect( slot() )


# OUTPUT:
# hi
# connect will call slot....
# Error: None is not callable



