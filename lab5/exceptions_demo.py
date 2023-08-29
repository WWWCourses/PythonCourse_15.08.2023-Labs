# Error(Syntax and Runtime(Exception)) vs Bug

# Syntax error:
# print(1)
# print('2)
# print(3)

# Runtime (Exception):
# print(1)
# print(5/0)
# print(3)

# bug - works, but not as excpected
# x = input('Enter an inetger:')
# res = x*2
# print( f'x*2={res}')

try:
	user_age = int(input('Enter your age:'))
except:
	print('Please, enter a number!!!!')
	exit()

print('END')




