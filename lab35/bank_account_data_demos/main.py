import json

from pymongo import MongoClient

def save_as_JSON_file(filename, data):
	with open(filename,'w') as f:
		json.dump(data, f, indent=4)

def save_in_mongodb(db_name,collection, data):
	# connect :
	conn_string='mongodb://localhost:27017/usersdb'
	db = MongoClient(conn_string)
	print(db.list_database_names())

if __name__=='__main__':
	# GIVEN:
	# Pesho => 100
	# Ada   => 50
	# Maria => 200

	user_accounts = [
		({
			'name':'Pesho',
			'balance': 100
		}),
		{
			'name':'Ada',
			'balance': 50
		},
		{
			'name':'Maria',
			'balance': 200
		},
	]


	# save_as_JSON_file('users.json', users)
	save_in_mongodb(
		db_name='usersdb',
		collection='user_accounts',
		data=user_accounts)

