# TASK: create function which returns the sum of square of VARIABLE bumber of arguments

# def sum_of_squares(*l):
# 	# l = (1,)
# 	# l = (1,2)

# 	return sum( [el**2 for el in l] )

# print(sum_of_squares( 1 )  )     	 # 1
# print(sum_of_squares( 1,2 ) )      # 1**2 + 2**2
# print(sum_of_squares( 1,2,3 ) )    # 1**2 + 2**2 +3**2


# def greet(name, age, *args):
# 	print(f'Hello, {name}, {age}')
# 	if args:
# 		print(f'{args[0]}')

# greet('Ada', 23)
# greet('Ada', 23, 'Sofia')
# greet('Ada', 23, 'Sofia', 'red')

# def greet(name, age, **kw):
# 	print(f'Hello, {name}, {age}')
# 	if kw:
# 		print(f'{kw["t"]}')

# greet('Ada', 23)
# greet('Ada', 23, t='Sofia')
# greet('Ada', 23, t='Sofia', c='red')


# def double(x):
# 	return x**2

# double = lambda x:x*2


# l = [
# 	(2,3),
# 	(5,2),
# 	(1,1),
# 	(1,4)
# ]

# def sorted(iterable, key=None):
# 	for el in iterable:
# 		print(key(el))

# def lot_sort(t):
# 	return t[1]


# sorted(l, key=lot_sort)
# sorted(l, key=lambda t:t[1])


# def dict(**kwarg)
# def dict(itterable, **kwarg)
# {'a':1}
# d = dict( [('a',1),('b',2)],c=3, d=4 )
# print(d)
# # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# for value in d:
# 	print(value)

# for key in d:
# 	print(key)



