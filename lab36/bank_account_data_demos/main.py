import json
from re import U

from pymongo import MongoClient

def save_as_JSON_file(filename, data):
	with open(filename,'w') as f:
		json.dump(data, f, indent=4)

def get_account_from_json(filename):
	with open(filename, 'r') as f:
		return json.load(f)

def save_in_mongodb(db_name,collection, data):
	# connect :
	conn_string='mongodb://localhost:27017/usersdb'
	db = MongoClient(conn_string)
	print(db.list_database_names())


if __name__=='__main__':

	user_accounts = get_account_from_json('./users.json')

	new_user = {
		'name': 'Asen',
		'balance':500
	}
	user_accounts.append(new_user)
	print(user_accounts)
	save_as_JSON_file('./users.json', user_accounts)



	# # save_as_JSON_file('users.json', users)
	# save_in_mongodb(
	# 	db_name='usersdb',
	# 	collection='user_accounts',
	# 	data=user_accounts)

	# TASK: get user names and balance, for those users whos name starts with 'A' and their balance >=100
