import mysql.connector

# Establish a connection to the MySQL server
db = mysql.connector.connect(
  host="localhost",
  port=3306,
  user="test",
  password="test1234",
  database="Tmp"
)

# Create a cursor object to interact with the database
cursor = db.cursor()

# insert_not_good_sql = """
# INSERT INTO students (student_name, student_age, student_grade)
# VALUES
# 	("Alice", 20, 4),
#   	("Bob", 22, 2),
#   	("Charlie", 21, 5),
#   	("Diana", 23, 6)
# """

# cursor.execute(insert_not_good_sql)
# db.commit()

# Data to be inserted into the table
student_data = [
  ("Alice", 20, 4),
  ("Bob", 22, 2),
  ("Charlie", 21, 5),
  ("Diana", 23, 6)
]

# # SQL query to insert data into the 'students' table
insert_query = """
INSERT INTO students (student_name, student_age, student_grade)
VALUES (%s, %s, %s)
"""

# Execute the query to insert data
cursor.executemany(insert_query, student_data)

# Commit changes to the database
db.commit()

# Close connection
db.close()
