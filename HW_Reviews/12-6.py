# Задача 6. Да се напише програма, която да сортира списък от tuples използвайки Lambda, (използвайки вторите елементи на tuples)

lot = [
	(1,2),
	(1,1),
	(4,3),
	(2,0)
]

# Variant 1 - standard function
def sort_by_second(t):
	return t[1]

lot_sorted = sorted( lot, key=sort_by_second )
print( lot_sorted )

# Variant 2 - lambda function
lot_sorted = sorted( lot, key=lambda t:t[1])
print( lot_sorted )


# # sort_by_second( (1,2) ) # 2
# # sort_by_second( (1,1) ) # 1
# # sort_by_second( (4,3) ) # 3