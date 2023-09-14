# ---------------------------- List Comprehensions --------------------------- #
# task: make evens list from list of numbers

# print('Variant with loops - not Pythonic')
# l = [1,2,3,4,5,6]

# evens = []
# for el in l:
# 	if el%2==0:
# 		evens.append(el)

# print(evens) # [2,4,6]

# print('Variant with list comprhensions:')
# l = [1,2,3,4,5,6]

# evens = [ el for el in l if el%2==0 ]

# print(evens) # [2,4,6]

# ------------------------- Dictionary comprhensions ------------------------- #
# keys = 	 ['1', '2', '3']
# values = ['Ivan', 'Asen', 'Ada']

# # make dictionary
# print('Variant with loops - not Pythonic')
# d = {}
# for idx,key in enumerate(keys):
# 	d[key] = values[idx]

# print(d)

# print('Variant with list comprhensions:')
# d = { key:values[idx] for idx,key in enumerate(keys )}
# print(d)

