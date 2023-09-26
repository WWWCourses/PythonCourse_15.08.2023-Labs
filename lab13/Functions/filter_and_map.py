# # filter l by evens
# l = [1,2,3,4]


# l_sorted = sorted(l, key=lambda x: x**2)


# def is_even(x):
# 	# if x % 2 != 0:
# 	# 	return False
# 	# else:
# 	# 	return True

# 	return x % 2 == 0




# # print( is_even(2) ) # True
# # print( is_even(3) ) # False

# l_filtered = filter(is_even, l)
# print(list(l_filtered))

# l_filtered = filter(lambda x:x % 2 == 0, l)
# print(list(l_filtered))


# list comprehension:
# evens = [ el for el in l if el%2==0 ]
# print(evens)