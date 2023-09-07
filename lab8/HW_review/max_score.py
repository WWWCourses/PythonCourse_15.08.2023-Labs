user_names = []
user_scores = []

# Prompt for user input:
while True:
	# Get valid user name:
	while True:
		user_name = input('Enter a name: ')
		if user_name.isalpha():
			user_names.append(user_name)
			break
		else:
			print('User name can be only letters: a-z')

	# Get user score:
	while True:
		try:
			user_score = int(input('Enter score: '))
			user_scores.append(user_score)
			break
		except:
			print('Please, enter an integer!')

	# enter another user?
	ans = input('Continue [y/n]: ')
	if ans.lower() != 'y':
		break


max_score = max(user_scores)
max_index = user_scores.index(max_score)

print(user_names[max_index])




