import random

# Implement "Guess the number game":

# generate machine random number in [1,10]
machine_number = random.randint(1,10)
print(f'machine_number={machine_number}')

user_number = int(input('Enter a number: '))

if user_number==machine_number:
	print('Bravo.You guessed!')
elif user_number<machine_number:
	print(f'{user_number} is to low')
else:
	print(f'{user_number} is to hight')


