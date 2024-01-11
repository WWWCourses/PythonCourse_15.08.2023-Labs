import mysql.connector
# from mysql.connector import connection


class DB:
	def __init__(self,user, password, db, host="localhost", port=3306):
		try:
			self.cnx = mysql.connector.connect(
				user=user,
				password=password,
				db=db,
				host=host,
				port=port
			)

		except mysql.connector.Error as e:
			print(e)

		print('*** Connection Established ***')


	def authenticate(self, cnx, user_name, password):
		# create a cursor for the connection
		cur = self.cnx.cursor()

		# prepare SQL query:
		q = f"""
			SELECT * FROM users
				WHERE username='{user_name}'
				AND `password`='{password}'
		"""
		# execute the query
		cur.execute(q)

		# we are only interested if 1 or 0 rows are returned
		res =  cur.fetchone()

		# do something with the result
		if(res):
			print('Authentication Successful')
		else:
			print('Authentication Failed')


if __name__ == '__main__':
	cnx = make_connection('root', '1234','car_shop_db')

	# let's use some hard-coded values for test:
	user_name = 'Maria'
	password = 'maria123'

	authenticate(cnx, user_name=user_name, password=password)



