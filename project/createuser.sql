#Script to create a user called "dbuser" with rights to the datebase called "theverge"
CREATE USER IF NOT EXISTS 'dbuser'@'localhost' IDENTIFIED BY 'dbpass';
GRANT SELECT, UPDATE, DELETE, INSERT ON theverge.* TO dbuser@localhost;
