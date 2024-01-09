import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user= "root",
    passwd = ""
)
print(conn)
cur = conn.cursor()
re = cur.execute("show databases")
r = cur.fetchall()
print(re)
print(type(re))
print(r)
print(type(r))
re = cur.execute("create database test2")
print("again")
re = cur.execute("show databases")
r = cur.fetchall()
print(re)
print(type(re))
print(r)
print(type(r))

