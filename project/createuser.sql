CREATE USER IF NOT EXISTS 'dbuser'@'localhost' IDENTIFIED BY 'dbpass';
GRANT SELECT, UPDATE, DELETE, INSERT ON theverge.* TO dbuser@localhost;
