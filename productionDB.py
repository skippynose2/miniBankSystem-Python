#Production database manager
import mysql.connector
db = mysql.connector.connect(
        host="localhost",
        user="main",
        password="FNkFngOW4fCFGKhi",
        database = "bank"
    )

print("connected to............")
print(db)
cursor = db.cursor()


def Add(USERNAME, AMOUNT):
    sql = "UPDATE ACCOUNTS SET AMOUNT = {} WHERE NAME= '{}'" .format(AMOUNT, USERNAME)
    cursor.execute(sql)
    db.commit()


def Fetch(USERNAME):
    sql = "SELECT PASSWORD, AMOUNT FROM ACCOUNTS WHERE NAME='{}'".format(USERNAME)
    cursor.execute(sql)
    results = cursor.fetchall()
    return results

def NewAccount(USERNAME, PASSWORD):
    sql = "INSERT INTO ACCOUNTS (NAME, PASSWORD, AMOUNT) VALUES (%s, %s, %s)"
    val = (USERNAME, PASSWORD, 0)
    cursor.execute(sql, val)
    db.commit()


