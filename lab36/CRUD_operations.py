import pymongo
from datetime import datetime
from pprint import pprint


class DB:
	def __init__(self) -> None:
		pass
		# # connect to server:
		self.client = pymongo.MongoClient('mongodb://localhost:27017')
		# client = pymongo.MongoClient('mongodb+srv://PythonCourse:12345678abv@cluster0.qprcu.mongodb.net/')

		# Create/Use db : 'new-db'
		self.db = self.client['new-db']

	def show_databases(self):
		print(self.client.list_database_names())

	def list_all_collection(self):
		print(self.db.list_collection_names())

	def insert_document(self):
		# inser a document into a new collection:
		doc_id = self.db.test_collection.insert_one({'a':1})
		print(doc_id.inserted_id)
	def insert_many_documents(self, data):
		self.db.todos.insert_many(data)
	def find_first(self):
		return self.db.todos.find_one()
	def find_all_and(self):
		return self.db.todos.find(
		{
			'$and':[
				{'priority':{'$gt':1}},
				{'completed':False}
			]
		},
		{
			'_id':0
		})

	def find_all(self):
		return self.db.todos.find({}, {'_id':0})

	def update_many(self):
		res = self.db.todos.update_many(
			{'priority':3},
			{'$set':
				{'priority':1}
			}
		)
		print(res.matched_count)

	def delete_one(self):
		res = self.db.todos.delete_one(
			{'completed':True}
		)

	def text_index_demo(self):
		# self.db.todos.create_index('title')
		self.db.todos.create_index([
			("title")
		])

		# TODO: fix error
		res = self.db.todos.find({ "$text": { "$search": "Learn" } })

		print(list(res))



if __name__=='__main__':
	db = DB()
	# db.update_many()
	# db.delete_one()
	# pprint(list(db.find_all()))
	db.text_index_demo()



