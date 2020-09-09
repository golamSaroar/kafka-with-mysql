import MySQLdb as mdb
import sys
from dateutil.parser import parse
from config import mysql

con = mdb.connect(mysql["host"], mysql["user"], mysql["password"], mysql["database"])

def createTable():
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS articles")
    cur.execute("CREATE TABLE articles(id INT PRIMARY KEY AUTO_INCREMENT, \
                link VARCHAR(255), \
                categories VARCHAR(100), \
                date_published DATETIME, \
                date_modified DATETIME, \
                headline VARCHAR(100), \
                short_description VARCHAR(500), \
                full_description VARCHAR(10000))")

def insertRow(data):
    cur = con.cursor()

    sql = "INSERT INTO articles(link, categories, date_published, date_modified, headline, short_description, full_description) \
        VALUES(%s, %s, %s, %s, %s, %s, %s)"

    link = data.get("link")
    categories = data.get("categories")
    date_published = parse(data.get("date_published")).strftime('%Y-%m-%d %H:%M:%S')
    date_modified = parse(data.get("date_modified")).strftime('%Y-%m-%d %H:%M:%S')
    headline = data.get("headline")
    short_description = data.get("short_description")
    full_description = data.get("full_description")

    values = (link, categories, date_published, date_modified, headline, short_description, full_description)

    cur.execute(sql, values)
    con.commit()

def fetchAll():
    cur = con.cursor()
    cur.execute("SELECT * FROM articles")

    rows = cur.fetchall()

    for row in rows:
        print(row)

