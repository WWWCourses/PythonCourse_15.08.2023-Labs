CREATE USER 'employees_db_admin'@'localhost' IDENTIFIED BY '!Employees_db_admin1234';

GRANT ALL PRIVILEGES ON *.* TO 'employees_db_admin'@'localhost';

FLUSH PRIVILEGES;

DROP user IF EXISTS'employees_db_admin'@'localhost';

SELECT user,host FROM mysql.user;


