CREATE USER 'dbuser'@'localhost' IDENTIFIED BY 'dbpass';
GRANT SELECT, UPDATE, DELETE, INSERT ON theverge.* TO dbuser@localhost;