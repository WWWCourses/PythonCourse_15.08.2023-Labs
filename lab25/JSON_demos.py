import json

# users = [
# 	{
# 		'id': 1,
# 		'name':'Kalin',
# 		'address':{
# 			'country': 'BG',
# 			'town':'Sofia'
# 		}
# 	},
# 	{
# 		'id': 2,
# 		'name':'Asen',
# 		'address':{
# 			'country': 'UK',
# 			'town':'London'
# 		}
# 	}
# ]


# # save data to file
# with open('user_accounts_dict.json', 'w') as f:
# 	json.dump(users,f)

# read data from file:
with open('user_accounts_dict.json', 'r') as f:
	users = json.load(f)
	print(users)





