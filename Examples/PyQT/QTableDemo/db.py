import mysql.connector
from pprint import PrettyPrinter

class DB:
	def __init__(self,user, password, db, host="localhost", port=3306)->None:

		# from mysql.connector import connection
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


	def insert_row(self, user_name, password):
		print(f'user_name: {user_name}')
		print(f'password: {password}')

		cur = self.cnx.cursor()
		# INSERT INTO users (username,password) VALUES('Maria','12')
		q = f"""
			INSERT INTO users (username,password) VALUES(%s,%s)
		"""

		res = cur.execute(q, (user_name,password))
		self.cnx.commit()
		print(res)

	def create_user_table(self):
		cur = self.cnx.cursor()
		q = """
			DROP TABLE IF EXISTS `users`;

			CREATE TABLE `users` (
			`id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'primary key',
			`username` varchar(50) NOT NULL,
			`password` varchar(45) NOT NULL,
			PRIMARY KEY (`id`)
			) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
			/*!40101 SET character_set_client = @saved_cs_client */;
		"""

		cur.execute(q)

		# DROP TABLE IF EXISTS `users`;
		# /*!40101 SET @saved_cs_client     = @@character_set_client */;
		# /*!40101 SET character_set_client = utf8 */;
		# CREATE TABLE `users` (
		# `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'primary key',
		# `username` varchar(50) NOT NULL,
		# `email` varchar(20) NOT NULL,
		# `password` varchar(45) NOT NULL,
		# PRIMARY KEY (`id`),
		# UNIQUE KEY `email` (`email`)
		# ) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
		# /*!40101 SET character_set_client = @saved_cs_client */;

	def select_all_data(self)->list:
		cur = self.cnx.cursor()
		q = "select * from users;"
		cur.execute(q)
		res = cur.fetchall()
		return res

if __name__ =='__main__':
	pp = PrettyPrinter()
	db = DB(user='test', password='test1234', db='pyqt_users_db')

	data = db.select_all_data()
	pp.pprint(data)
