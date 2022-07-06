-- Crete a user and set password
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
