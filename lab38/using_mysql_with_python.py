from matplotlib import artist
import mysql.connector

# ----------------------------- connect to server ---------------------------- #
def make_connection():
	conn_date = {
		'user':'test',
		'password':'test1234',
		'host':'localhost',
		'port':3306,
		'database':'Tmp'
	}

	return mysql.connector.connect(**conn_date)

def select_all(conn):
	cursor = conn.cursor()
	cursor.execute('SELECT * from artist WHERE age>23  ')
	rows  = cursor.fetchall()
	for row in rows:
		print(row)

def insert_data(conn):
	cursor = conn.cursor()
	# TODO: fix error
	cursor.execute('''
		INSERT INTO artist VALUES(fname, lname, age)
			('Ada', 'Byron', 23),
			('Pesho', 'Petrov', 34);
	''')

	conn.commit()

con = make_connection()

# -------------------------------- INSERT DATA ------------------------------- #
insert_data(con)
select_all(con)


con.close()


