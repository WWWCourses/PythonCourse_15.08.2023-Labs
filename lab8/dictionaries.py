# users = ['ada', 'pesho', 'maria']

# 0: 'ada'
# 1: 'pesho'
# 2: 'maria'

# data with list:
# ada_list = [
# 	'Ada',
# 	34,
# 	'Bulgaria'
# ]

# ada_dict = {
# 	0:'Ada',
# 	1:34,
# 	2:'Bulgaria'
# }
# print(ada_dict[1])

# 0: 'Ada'
# 1: 34
# 2: 'Bulgaria'
# print( ada_list[1] )

# data with dictionary:

# ada_dict = {
# 	'name':'Ada',
# 	'age':34,
# 	'country':'Bulgaria',
# }



# ada:
# 'name': 'Ada'
# 'age': 34
# 'country': 'Bulgaria'

# get age:
# print( ada_dict['town'] )
# print( ada_dict.get('town', 'Sofia') )



#TASK: Represent next data:
# Maria - 4
# Ivan  - 3
# Peter - 5


# Variant1 - the worst
# users_data = [
# 	['Maria',4],
# 	['Ivan',3],
# 	['Peter',5],
# ]

# Varaint2: List Of Lists:
# users_data_LOL = [
# 	['Maria', 'Ivan', 'Peter'],
# 	[4,3,5]
# ]

# print( f'{users_data[0][2]} - {users_data[1][2]}')

# Variant3: List of dictionaries
# users_data_LOD = [
# 	{'name':'Maria','score':4},
# 	{'name':'Ivan','score':3},
# 	{'name':'Peter','score':5},
# ]



# print( f"{users_data_LOD[2]['name']} - {users_data_LOD[2]['score']}")

# ada_dict = {
# 	'name':'Ada',
# 	'age':34,
# 	'countries':['Bulgaria','UK','France'],
# }
# # print the number of countries
# print( len(ada_dict['countries']) )

# ---------------------------- Dictionary creating --------------------------- #

# d1 = {}
# print( type(d1) )

# d1 = dict()
# print( type(d1) )

# ------------------------ Dict methods and operations ----------------------- #
# d = {'age':34}
# # add key:value in dict
# d['name'] = 'Maria'
# # update value by
# d['age'] = 99
# print(d)

# Remove element by key
# d = {'age':34, 'name': 'Maria'}
# # del d['age']
# age = d.pop('age')
# print(d)
# print(age)


# ----------------------------- Copy dictionaries ---------------------------- #
# l_copy = l1[:]
# user_data = {'age':34, 'name': 'Maria'}
# # this is not a copy
# # user_data_copy = user_data
# user_data_copy = user_data.copy()
# user_data['age'] = 90
# print(user_data)
# print(user_data_copy)

















