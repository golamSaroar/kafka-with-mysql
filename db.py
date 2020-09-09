import MySQLdb as mdb
import sys
from config import mysql

con = mdb.connect(mysql["host"], mysql["user"], mysql["password"], mysql["database"])

def createTable():
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS articles")
    cur.execute("CREATE TABLE articles(id INT PRIMARY KEY AUTO_INCREMENT, \
                 number INT(4))")

def insertRow(data):
    cur = con.cursor()
    columns = ",".join(data.keys())
    values = ",".join(str(v) for v in data.values())
    cur.execute("INSERT INTO articles({}) VALUES({})".format(columns, values))
    con.commit()

def fetchAll():
    cur = con.cursor()
    cur.execute("SELECT * FROM articles")

    rows = cur.fetchall()

    for row in rows:
        print(row)

