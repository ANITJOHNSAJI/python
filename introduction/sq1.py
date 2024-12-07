import sqlite3
conn=sqlite3.connect('exmple.db')
cursor=conn.cursor()
# cursor.execute("CREATE TABLE STUDENT(ROLLNO text,Name text)")
data=[('2','james'),('3','messi'),('10','neymar')]
cursor.executemany("INSERT INTO STUDENT (ROLLNO,Name) VALUES(?,?)",data)
conn.commit()
conn.close()
print("Data Inserted")