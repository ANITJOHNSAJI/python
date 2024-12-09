import sqlite3
conn=sqlite3.connect('exmple.db')
cursor=conn.cursor()
# cursor.execute("CREATE TABLE STUDENT(ROLLNO text,Name text)")
# data=[('2','james'),('3','messi'),('10','neymar')]
# cursor.executemany("INSERT INTO STUDENT (ROLLNO,Name) VALUES(?,?)",data)
# conn.commit()
# conn.close()
# print("Data Inserted")

# 9/12/24

# p=cursor.execute("SELECT * FROM STUDENT")
# for i in p:
#     print(i)
# conn.commit()
# conn.close()

# p=cursor.execute("SELECT Name FROM STUDENT")
# for i in p:
#     print(i)
# conn.commit()
# conn.close()

# p=cursor.execute("SELECT Name FROM STUDENT WHERE rollno>2")
# for i in p:
#     print(i)
# conn.commit()
# conn.close()

# p=cursor.execute("UPDATE STUDENT SET ROLLNO = 4 WHERE Name ='neymar' ")
# conn.commit()
# conn.close()

# p=cursor.execute("UPDATE STUDENT SET Name = 'Ramos' WHERE ROLLNO = 4 ")
# conn.commit()
# conn.close()

# p=cursor.execute("DELETE FROM STUDENT WHERE Name = 'james' ")
# conn.commit()
# conn.close()

# p=cursor.execute("SELECT MAX(ROLLNO)FROM STUDENT ")
# for i in p:
#      print(i)
# conn.commit()
# conn.close()

# p=cursor.execute("SELECT Name,COUNT(*)FROM STUDENT GROUP BY Name ")
# for i in p:
#      print(i)
# conn.commit()
# conn.close()

# data=[('2','Neymar'),('5','Suarez')]
# cursor.executemany("INSERT INTO STUDENT (ROLLNO,Name) VALUES(?,?)",data)
# conn.commit()
# conn.close()
# print("Data Inserted")

# p=cursor.execute("SELECT * FROM STUDENT ORDER BY ROLLNO ")
# for i in p:
#      print(i)
# conn.commit()
# conn.close()

#table delete cheyyan
# p=cursor.execute("DROP TABLE STUDENT ")
# for i in p:
#      print(i)
# conn.commit()
# conn.close()
