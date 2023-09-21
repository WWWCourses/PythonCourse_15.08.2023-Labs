# y = sin(x) + sum(2,3)

# ---------------------------- Function definition --------------------------- #
# def say_hello(user_name):
# 	print('*' * 30)
# 	print(f'Hello, {user_name}')
# 	print('*' * 30)


# x  = 1
# RAM:
# 	say_hello: 01010101010100
#             x: 00010100000000

### say hello to the user:

# say_hello('Ada')
# say_hello('Pesho')


# def sum(x,y):
# 	# x = 2
# 	# y = 3
# 	print(x+y)

# sum(2,3)
# a,b = 5,10
# sum( a**3,b )



# def say_hello(name, family):
	# print('*' * 30)
	# print(f'Hello, {name} {family}')
	# print('*' * 30)

# say_hello('Ada','Byron')
# say_hello(4,5)


# def change_list_element(l):
# 	# l = data
# 	l[0] = 9


# data = [1,2,3]
# change_list_element(data)
# print(data)


# def change_int(x):
# 	# x = y
# 	x = 9

# y = 0
# change_int(y)
# print(y) # ?


# ----------------------------- Default parameters ---------------------------- #
# def foo(x=1):
# 	print(x)

# foo()
# foo(2)
# foo(3)

# def say_hello(name, family=""):
# 	print('*' * 30)
# 	print(f'Hello, {name} {family}!')
# 	print('*' * 30)

# say_hello('Ada', 'Byron')
# say_hello('Pesho')


# def foo(y, x=1):
# 	print(x, y)

# foo(2)   #
# foo(3,4)

# ----------------------------- Keyword Arguments ---------------------------- #
# def foo(base,exp):
# 	print(base**exp)


# foo(2,3)
# foo(exp=3,base=2)

# def foo(x,y,z):
# 	print(x,y,z)

# foo(2, z=3, y=1 )


# ------------------------ Variable parameters (*args) ----------------------- #
# def add(*l):
# 	# l = (1,2)
# 	print(sum(l))


# add( 1,2 ) 		# 3
# add( 1,2,3 ) 		# 6
# add( 1,2,3,4 ) 	# 10

# def foo(*args):
# 	print(args[0])

# foo(1)    #
# foo(1,2)
# # foo()


# def foo(x, *args, y=9):
# 	print(x)   		#1
# 	print(args)     #(2,)
# 	print(y)        #(9)

# foo(1,2)


# ------------------------ Variable parameters (**kwargs) ----------------------- #
# def foo(**kwargs):
# 	print(kwargs)

# foo()
# foo(x=1)
# foo(x=1,y=2)


# def greet(**kwargs):
# 	print(kwargs['age'])

# greet(name='Ada',age=23,score=51)


# # user_data = {
# # 	'name':'Ada',
# # 	'age': 23
# # }


# def foo(x, *args,**kwargs):
# 	print(x)				# 1
# 	print(args)				# (2,3,4,5)
# 	print(kwargs) 			# {'y':1}


# foo(1,2,3,4,5,y=1)

# --------------------------- Function Return Value -------------------------- #
# def add(x,y):
# 	print(111111)
# 	return(x+y)


# res = add(2,3) + add(4,5)
# print(res)


# ----------------------------- Ternary operatory ---------------------------- #
# user_age = 17
# status = ""
# if user_age>=18:
# 	status = 'adult'
# else:
# 	status = 'child'

# status = 'adult' if user_age>=18 else 'child'



# def find_status(user_age):
# 	return 'adult' if user_age>=18 else 'child'

# print( find_status(34) )
# print( find_status(12) )

# def is_adult(age):
# 	return True if age>=18 else False

# if is_adult(34):
# 	print('Welcome')

