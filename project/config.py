import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="dbuser03",
    passwd="dbpass",
    db="theverge",
    buffered=True)
