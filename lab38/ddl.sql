show DATABASES;

-- CREATE TABLE table_name(
--   column_name1 data_type,
--   column_name2 data_type,
--   ....
-- );

-- CREATE TABLE ADMIN(
-- 	name:VARCHAR(20),
-- 	mail:VARCHAR(30)
-- );

-- id|name|mail
-- 1|'ada'|'ada@gmail'
-- 2|'ada'|'ada@gmail'

use Tmp;

drop TABLE IF EXISTS artist;

CREATE TABLE artist (
--   artist_id SMALLINT(5) NOT NULL DEFAULT 0,
  fname CHAR(20) DEFAULT NULL,
  lname VARCHAR(20) NOT NULL DEFAULT 'Anonymous',
  age TINYINT UNSIGNED DEFAULT NULL
--   balance BIGINT(10) DEFAULT NULL,
--   salary DECIMAL(5,2) UNSIGNED DEFAULT NULL,
--   color ENUM('red', 'green', 'blue') DEFAULT NULL,
--   birthdate DATE,
--   birthdatetime TIMESTAMP
);

INSERT INTO artist(birthdate, birthdatetime) VALUES
('2023.12.25', '2023.12.25T12:10:55');

SELECT * from artist;

use employees;

show tables;

show CREATE TABLE employees.employees;

drop DATABASE test;

CREATE DATABASE test;