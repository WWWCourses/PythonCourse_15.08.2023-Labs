# Задача 1. Да се напише програма, която сортира в нарастващ ред списък, чиито елементи
# са tuples. При сортирането да се взема предвид последният елемент във всеки tuple. В
# списъкът не трябва да се съдържат празни tuples.

# Вход: [
	# (2, 5),
	# (1, 2),
	# (4, 4),
	# (2, 3),
	# (2, 1)
# ]
# Изход: [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# sorted(iterable, /, *, key=None, reverse=False)


input_list = [
	(2, 5),
	(1, 2),
	(4, 4),
	(2, 3),
	(2, 1)
]

# variant 1:
# sorted_list = sorted(input_list, key=lambda t:t[1])
# print(sorted_list)

# variant 2:
for el in input_list:
	### TODO: implement bubble sort




# t1 = (2, 5)
# print(t1.__getitem__(1))

