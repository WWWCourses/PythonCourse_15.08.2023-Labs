SELECT * FROM artist;

ALTER TABLE artist ADD INDEX(fname);

DESC artist;

SELECT * FROM artist
WHERE fname='Ada';

DROP TABLE artist;

### One-to-Many Ralationship

# define the Parent Table
DROP TABLE orders;
DROP TABLE customers;

CREATE TABLE `customers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45),
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8;

# define the Child Table
CREATE TABLE `orders` (
  `id` int NOT NULL AUTO_INCREMENT,
  `customer_id` int NOT NULL,
  `order_date` datetime NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`)
) DEFAULT CHARSET=utf8;

INSERT INTO customers (first_name)
VALUES 	('Pesho'),
		('Maria'),
		('Asen');

INSERT INTO orders (customer_id, order_date)
VALUES 	(1, '2012.02.23'),
		(1, '2023.02.23'),
		(2, '2023.03.23');




SELECT c.first_name, o.order_date
FROM customers as c, orders as o
WHERE c.first_name='Pesho' AND c.id=o.customer_id;



### Many-to-many relationship
CREATE TABLE artist (
  id MEDIUMINT(4) NOT NULL AUTO_INCREMENT,
  address_id INT(4) NOT NULL,
  fname VARCHAR(20) DEFAULT NULL,
  lname VARCHAR(20) NOT NULL,
  email VARCHAR(20) NOT NULL UNIQUE,
  age SMALLINT UNSIGNED DEFAULT 0,
  INDEX (fname),
  PRIMARY KEY(id),
  FOREIGN KEY (address_id) REFERENCES address (id)
);

CREATE TABLE address (
	id INT(4) NOT NULL AUTO_INCREMENT,
	artist_id MEDIUMINT(4) NOT NULL,
	country VARCHAR(10),
  	town VARCHAR(20)
	PRIMARY KEY (id),
	FOREIGN KEY (artist_id) REFERENCES artist (id)
);
ny-