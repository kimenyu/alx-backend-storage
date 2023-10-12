--Write a SQL script that creates a table users following these requirements:
--With these attributes:
--id, integer, never null, auto increment and primary key
--email, string (255 characters), never null and unique
--name, string (255 characters)
--If the table already exists, your script should not fail
--Your script can be executed on any database

CREAT TABLE users IF NOT EXISTS (
	id INT NOT NULL AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255)
	);
