# -------------------------- Expression vs Statement ------------------------- #
# Expression => calculated to value
# 2+3
# print(2+3)

# x = 10
# x>5
# print(x>5)
# print(9>3)

# Stetement => do something
# x = 2
# print(x = 2)


# print('Hello')
# print('World')

# --------------------------- Convert to data type --------------------------- #
# string to integer
# x = '6'
# x = int(x)
# print('6')
# print( int('6') )
# print( int(6.99) )

# print( str(6) + '2')


# ------------------------------- IF Statement ------------------------------- #
# TASK:
# if the user is adult => print('Welcome')
# if the user is not adult => print('Go home')
# user_age = 42

# Not good solution:
# if user_age>=18:
# 	print('Welcome')

# if not (user_age>=18):
# 	print('Go home')

# the wright way:
# user_age = 42

# if user_age>=18:
# 	print('Welcome')
# else:
# 	print('Go home')


#TASK:
# if x is even => print('Even')
# if x is odd => print('Odd')

# x = 6
# x = int(input('x='))
# print( type(x) )

# if x%2==0:
#     print('Even')
# else:
#     print('Odd')

#TASK:
# if x is zero => print('Zero')
# if x is even => print('Even')
# if x is odd => print('Odd')

# Not good:
# x = 9

# if x==0:
#      print('Zero')
# else:
#     if x%2==0:
#         print('Even')
#     else:
#         print('Odd')

# The best variant

# x = 10

# if x==0:
#     print('Zero')
# elif x%2==0:
#     print('Even')
# else:
#     print('Odd')


# ------------------------------ IF in one line ------------------------------ #
# if 5>3:print('Yes');print('Yes again')
# print('END')


# ------------------------------- Pass stamtent ------------------------------ #
# user_age = 12

# if user_age>=18:
#     pass
# # do main logic
# print('Test')


# ----------------------------- Ternary Operator ----------------------------- #
# expr1 if cond else expr2
# 'Adult' if user_age>=18 else 'Child'

# Variant without ternary operator:
# user_age = 49
# status = ''

# if user_age>=18:
# 	status = 'Adult'
# else:
# 	status = 'Child'

# print(f'Hi, you are {status}')

# Variant with ternary operator:

# user_age = 49
# status = 'Adult' if user_age>=18 else 'Child'

# print(f'Hi, you are {status}')

# ----------------------- What is True/False in Python ----------------------- #

# user_name = ''
# if user_name:
#     print(f'Hi {user_name}')
# else:
#     print(f' Hi, Anonymous')


# if 1:
#     print('hi')
#     print('hi')
#     print('hi')
#     print('hi')
#     print('hi')
#     print('hi')
#     print('hi')

# print( bool(-0.001) )
# print( bool(0) )

# if -0.001:
#     print('Hi')


# -------------------------- Logical operators demo -------------------------- #

# x or y	if x is false, then y, else x
# print( 3 or 3-4+1 ) # 3

# x = 18
# # x-18 and print('Hi')
# x-18 or print('Hi')


# --------------------------------- Examples --------------------------------- #
# print( 3 + 2 * 4)

# print(5>3 or 4<2 and 3==3 )
# print((5>3 or 4<2) and 3==3 )


