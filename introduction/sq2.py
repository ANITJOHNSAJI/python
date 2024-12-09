import sqlite3
conn=sqlite3.connect('exmple.db')
cursor=conn.cursor()
# cursor.execute("CREATE TABLE STUDENT2(ID text,NAME text,AGE text,CITY text)")
data=[('7','Riju','20','Ayarkunnam')]
cursor.executemany("INSERT INTO STUDENT2 (ID,NAME,AGE,CITY) VALUES(?,?,?,?)",data)
p=cursor.execute("UPDATE STUDENT2 SET CITY = 'Lakatoor' WHERE ID = 7 ")
conn.commit()
conn.close()
