# ------------------------------ Decrlaring sets ----------------------------- #
# l = [1,2,3,2,1]
# s = {1,2,3,2,1}
# s = set(l)

# print(l[0])
# print(s[0]) # sets are NOT ORDERED

# for el in s:
# 	print(el)

# string1 = 'abcccd'

# s = set(string1)

# print(s)


# s = {'1', [1]}
# print(s)


# -------------------------- Adding elements to set -------------------------- #
## add one:
# s = {1,2,3}
# s.add(4)
# print(s)

## add many:
# s = {1,2,3}
# s.add([4,5])
# print(s)
# print(len(s))

# Remove element from set:
# s = {1,2,3}
# s.discard(4)
# s.remove(4)

# print(s)
# s.pop()
# print(s)

# remove all:
# s = {1,2,3}
# s.clear()
# print(s)

# ------------------------------ Sets Operations ----------------------------- #
# users = {'Maria', 'Peter', 'Ivan', 'Anna'}
# womens = {'Maria', 'Ada'}

### Union:
# users_and_womens = users | womens
# users_and_womens = users.union(womens)
# users_and_womens = womens.union(users)
# print(users_and_womens)


### Intersection:
# users_which_are_womens = users & womens
# users_which_are_womens = users.intersection(womens)
# print(users_which_are_womens)

### Difference:
# users_without_womens = users - womens
# users_without_womens = womens - users
# users_without_womens = womens.difference(users)

# print(users_without_womens)

### Subsets (<, >, ==)
# print( users>womens )
# print( users<womens )

# s1 = {1,2,3}
# s2 = {2,3}

# print( s1>s2 )
# print( s2<s1 )















