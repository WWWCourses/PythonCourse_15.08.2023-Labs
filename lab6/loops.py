# TASK: print in console the numbers 1 ..9
# print(1)
# print(2)


# ---------------------------------- range() --------------------------------- #
# print( range(1,10,1) )
# print( list(range(1,10,1)) )

# print( list(range(1,10,2)) ) # 1,3,5,7,9

# print( list(range(10)) ) #
# print( list(range(1,10,1)) ) #


# print( list(range(3,5,2)) )  # 3
# print( list(range(4,0,-1)) ) # 4,3,2,1
# print( list(range(-4,0,-1)) ) # []

# -5, ....., 0, ....., 5


# --------------------------------- for loop --------------------------------- #

# for el in 'abc':
# 	print(el)

# print('END')

# for el in range(5):
# 	print(el)

# TASK: print 50 times 'hello':
# for _ in range(50):
# 	print('hello')


# ----------------------------- Nested for loops ----------------------------- #
# for i in range(3):
# 	for j in range(2):
# 		print(i,j)

# i = 0
# 	j = 0 -> 0 0
# 	j = 1 -> 0 1
# i= 1
# 	j = 0 -> 1 0
# 	j = 1 -> 1 1

# --------------------------------- Continue --------------------------------- #
# i = 0
# for letter in 'abc':
# 	print(letter,i)
# 	if i%2:
# 		continue
# 	i+=1


# a 0
# b 1
# c 1



# -------------------------------- while loop -------------------------------- #
# x = 0
# while x<6:
# 	print('Hello')
# 	x+=1

# for x in range(6):
# 	print('Hello')

# while - do
# x = int(input('Enter positive number:'))

# while x<=0:
# 	x = int(input('Enter positive number:'))

# print(f'x = {x}')

# do - while
while True:
	x = int(input('Enter positive number:'))
	if x>0:
		break
print(f'x = {x}')






