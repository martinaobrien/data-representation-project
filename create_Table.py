import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="datarepresentation"
)


cursor = db.cursor()
# The SQL is creating the table inside the database and adding the columns needed.
sql = "CREATE TABLE films(Id int not null AUTO_INCREMENT PRIMARY KEY,Film varchar(250) NOT NULL,Director varchar(250) NOT NULL,Year int NOT NULL)"
cursor.execute(sql)
db.commit()
print("###### Your Table is ready for use ########")