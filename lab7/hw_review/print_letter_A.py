# Задача 8. Да се принтира буквата A на екрана както е дадено по-долу:
#   ***
#  *   *
#  *   *
#  *****
#  *   *
#  *   *
#  *   *

middle = 5
top = 3
rows = 2*middle - top

for row in range(rows):
	if row==0:
		print(' ', '*' * 3, ' ', sep='')
	else:
		print('*', ' ' * top, '*', sep='')




