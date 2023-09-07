# ---------------------------------- remove ---------------------------------- #
# l = [1,2,3]
# l.remove(4)

# print(l)

# -------------------------------- min/max/sum ------------------------------- #
# l = [1,2,3]
# print( min(l) )
# print( max(l) )
# print( sum(l) )

# l = ['13', '2']
# print( max(l) )  # '2'

# lexicographical sorting:
# print( '13' > '2' )
# print( 'A' > 'a' )  # False
# print( 65 > 97 )  	# False


# ------------------------------- Sorting list ------------------------------- #
# 1. sorted() function
# l = [4,2,3,7]

# sorted_l = sorted(l, reverse=True)

# print(l)
# print(sorted_l)

# 2. list.sort() method

# l = [4,2,3,7]
# l.sort(reverse=True)
# print(l)

# ------------------------------- in and not in ------------------------------ #
# l = [2,3,1]

# print( 2 in l )
# print( 4 in l )

# print( 2 not in l )
# print( 4 not in l )



# check for full list:
# l = [1,3,2]
# if l:
# 	print('Not empty')

# check for empty list:
# l = []
# if not l:
# 	print('Empty')


# ------------------------------ Loops on lists ------------------------------ #
# TASK: find the index of min element

# Variant 1
# l = [1,2,3,4,-9]
# min_el = min(l)
# min_index = l.index(min_el)
# print(min_index)

# # Varint 2:
# l = [1,2,0,3,4,]
# min_index = 0
# min_number = l[0]

# idx=0

# for el in l:
# 	if el<min_number:
# 		min_number = el
# 		min_index = idx

# 	idx+=1

# for idx,el in enumerate(l):
# 	if el<min_number:
# 		min_number = el
# 		min_index = idx


# print(min_index)


# ------------------ Remove all occurences of given element: ----------------- #
# l = [2,1,3,1,5,1]
# l.remove(1)

# print(l)

# while 1 in l:
# 	l.remove(1)

# print(l)

# ------------------------------- shallow copy ------------------------------- #

# l1 = [ [1],2,3 ]
# l2=l1[:]
# l1[0][0] = 9

# # l2 is not a full, byt shallow copy
# print(l2) # 1,2,3










