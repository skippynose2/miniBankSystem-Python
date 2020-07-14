import mysql.connector

#creating the database connection
mydb = mysql.connector.connect(
        host="localhost",
        user='main',
        password="akhil2003",
        database="bank"
    )



sql = "DELETE FROM ACCOUNTS WHERE NAME = 'Akhil'"
pointer = mydb.cursor()
pointer.execute(sql)
mydb.commit()

print("Connected too......")
print(mydb)
pointer = mydb.cursor()
#Inserts info into already made table
sql = "INSERT INTO ACCOUNTS (NAME, PASSWORD, AMOUNT) VALUES (%s, %s, %s)"
val = ("Akhil", "1234", 0)
pointer.execute(sql, val)
mydb.commit()

#!-------------IMPORTANT mydb.commit() is needed to make changes to the table or else no data is saved----------------------!!!!



sql = "DELETE FROM ACCOUNTS WHERE NAME = 'John'"
pointer = mydb.cursor()
pointer.execute(sql)
mydb.commit()

sql = "INSERT INTO ACCOUNTS (NAME, PASSWORD, AMOUNT) VALUES (%s, %s, %s)"
values = ("John", "12345", 0)
pointer.execute(sql, values)
mydb.commit()

#Getting data from database for specific row
pointer.execute("SELECT * FROM ACCOUNTS WHERE NAME = 'John'")
#Stored in an array 0 is name, 1 is password, 2 is amount
results = pointer.fetchall()
print(results)


#Getting data from the whole table
print("All data")
pointer.execute("SELECT NAME, PASSWORD, AMOUNT FROM ACCOUNTS")
results = pointer.fetchall()
print(results)

#Updating a value
sql = "UPDATE ACCOUNTS SET AMOUNT = 5000 WHERE NAME = 'Akhil'"
pointer.execute(sql)
mydb.commit()


#Delete a certain column
#sql = "DROP COLUMN AMOUNT WHERE NAME = 'John'"
#pointer.execute(sql)
#mydb.commit()

#Delete whole table user WHERE to only delete one thing
#sql = "DELETE FROM ACCOUNTS"
#pointer.execute(sql)
#mydb.commit()

