l = [1,2,3]

# l is itterable
# for el in l:
# 	print(el)


l_iterator = l.__iter__()
l_next = l_iterator.__next__()
print(l_next)

l_next = next(l_iterator)
print(l_next)

l_next = l_iterator.__next__()
print(l_next)

l_next = next(l_iterator) #Error
print(l_next)

# r_iter = iter(range(3))
# print( next(r_iter) )
# print( next(r_iter) )
# print( next(r_iter) )





