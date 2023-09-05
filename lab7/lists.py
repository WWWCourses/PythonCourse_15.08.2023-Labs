# ----------------------------------- NOTES ---------------------------------- #
# values (litterals):
# x = 5 - value of type int
# s = '5' -   value of type str
# l = ['Maria','Pesho', 'Ivan']


# RAM:
# 	x   : 00000011 (5)
#   l   :
# 	l[0]: 01000100 ('Maria')
# 	l[1]: 01000100 ('Pesho')
# 	l[2]: 01000100 ('Ivan')


# TASK: find student with max score:
# Maria - 5
# Pesho - 4
# Ivan - 6

# Sequence data types: List, String, Tupple

# ------------------------------- Create lists ------------------------------- #
# l1 = [] 		# empty list, 0 elements
# l2 = [1,2,3] 	# 3 elements
# l3 = [1, 'Ivan', True, 4.5] # 4 elements
# l4 = [1, 'Ivan', [2,3]] # 3 elements

# print(l2)
# print(l2[0])
# print(l2[1])
# print(l2[2])

# print(l4)
# print(l4[0]) # 1
# print(l4[1]) # 'Ivan
# print(l4[2]) #  [2,3]


# print(type(l4))     # class list
# print(type(l4[0]))  # class int
# print(type(l4[2]))  # class list



# --------------------------------- Indexing --------------------------------- #
# students = ['Maria','Pesho', 'Ivan', 'Asen']

# print( students[0] )
# print( students[-1] )
# print( students[-2] )
# print( students[-2+3] )


# change list element
# students[0] = 'Ada'
# students[-1] = 'Stoyan'
# print(students)

# l = [1, [2,3]]
# # task: print 3
# print( l[1][1] )

# l = [1, ['a', 'b', [4,5]]]
# print(len(l)) #
# task: print 'b' 5
# print(l[1],l[3][1]) #
# print(l[1][1], l[1][2][1])

# s = "As'e'n"
# print(len(s)) #
# print( s[0] )
# print( s[-1] )

# # l = [1, ['a', 'b', [4,5]]]
# # # task: change 5 to 9
# # l[1][2][1] = 9

# print(l) # [1, ['a', 'b', [4,9]]]

# -------------------------- Get identity of a value ------------------------- #
# x = 5
# print( id(x) )
# print( id(5) )

# x = 6
# print( id(x) )

# identity of list
# l = [5]


# --------------------------------- list copy -------------------------------- #
# print( id(l[0]) )
# l[0] = 6
# print( id(l[0]) )
# x = 5
# y = x # copy by value
# x = 4
#   : 123400000001: 5
#   y: 123400000001
#   x: 123400000009:4
# print(y) # 5

# x = [5]
# y = x # copy by reference
# x[0] = 4

# print(x)
# print(y)

# try to make a copy:
# student_names = ['Maria']
# # student_names_copy = student_names # this is NOT A COPY!!!
# # using slice for copy
# student_names_copy = student_names[:] # this IS A COPY

# student_names_copy[0] = 'Asen'
# print(student_names)
# print(student_names_copy)


# ---------------------------------- Slicing --------------------------------- #
# l[start:end:step]
# l[start:end] # step=1
# l[:end] # start=0, step=1
# l[start:] # end=last element, step=1
# l[:] # start=0. end=last element, step=1

# get first 2 elements in l2
# l = [1,2,3,4,5]
# l2 = l[0:2:1]
# l3 = l[:2]
# print(l2) #[1,2]
# print(l3) #[1,2]

# get all element except first:
# l = [1,2,3,4,5]
# l2 = l[1:]
# print(l2) # [2,3,4,5]

# Slice is a new list
# l[2] = 9
# print(l)
# print(l2)

# Copy list:
# l = [1,2,3,4,5]
# l2 = l[:]

# l[0] = 9

# print(l)
# print(l2)


# l = [1,2,3,4,5]

# get last 2 elements:
# l2 = l[-1:-3:1]
# l2 = l[-2:]
# print(l2)



# Loop on list:
# students = ['Maria','Pesho', 'Ivan', 'Asen']

# # print students elemets:
# # print(students[0])
# # print(students[1])
# # print(students[2])


# students_len = len(students)
# print(students_len)

# for i in range(students_len):
# 	print(students[i])

# s = 'abc'
# last_index = len(s) - 1
# print(s[last_index])

# print(s[-1])

# --------------------------- Add elements to list --------------------------- #
### list.apend(element)
# l = []
# l.append(3)
# l.append(4)
# print(l)


# TASK: add 5 user numbers into list:
# l = []
# for i in range(5):
# 	x = int(input('Enter a number:'))
# 	l.append(x)

# print(l)

# l = [1,2]
# l.append( [3,4] )
# print(l) # [1,2,[3,4]]

### list.insert(index,elemet )
# l = [1,2,3]
# l.insert(1,9)
# print(l)


# ------------------------ Remove elements from list: ------------------------ #
# l = [1,2,3]

# ### list.pop()
# x = l.pop()
# print(l)
# l.pop()
# # print(l)
# print(x)

### list.remove()

l = [1,2,3]
l.remove(4)
print(l)







