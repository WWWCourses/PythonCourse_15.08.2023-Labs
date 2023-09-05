
while True:
	student_name = input('Enter student name: ')

	try:
		student_score = int(input('Enter student score: '))
	except:
		print('Please, enter a number!')
		continue

	another = input('Enter another [Y/N]: ')
	if another.lower() != 'y':
		break
