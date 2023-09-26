# Задача 7. Да се напише програма, която да сортира списък от речници (by values) използвайки Lambda.

lod = [
	{'a': 3},
	{'b': 1},
	{'c': 2}
]

def sort_dict(d):
	# print( list(d.values())[0] ) # 3
	return list(d.values())[0]


# print( sort_dict( {'a': 3} ) ) # 3
# print( sort_dict( {'b': 1} ) ) # 1

lod_sorted = sorted(lod, key=sort_dict )
print(lod_sorted)


# with lambda:
lod_sorted = sorted( lod, key=lambda d: list(d.values())[0] )
print(lod_sorted)

# def sorted(iterable, f):
# 	for el in iterable:
# 		f()
