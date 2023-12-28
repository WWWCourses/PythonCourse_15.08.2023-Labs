SELECT fname,age
FROM artist
WHERE fname='Ada'
ORDER BY age
LIMIT 3;

SELECT * FROM artist;


DELETE FROM artist
WHERE fname='Ada';
-- [LIMIT row_count]

INSERT INTO artist (fname, lname, age, email)
VALUES
	('Ada', 'Byron', 23, 'ada@gmail.com'),
	('Maria', 'petrova', 34, 'maria@gmail.com');

UPDATE artist
SET lname='Petrova'
WHERE fname='Maria' AND age=32;

CREATE TABLE students (
	id INT NOT NULL AUTO_INCREMENT,
	student_name VARCHAR(15),
	student_age SMALLINT UNSIGNED,
	student_grade SMALLINT UNSIGNED NOT NULL,
	PRIMARY KEY (id)
)

