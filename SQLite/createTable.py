import sqlite3

conn=sqlite3.connect("tables.db")

# conn.execute("create table emp (id int primary key not null,name text not null,age int not null);")

conn.execute("insert into emp values(1,'Rohit',27);")

conn.execute("insert into emp values(2,'Omkar',27);")
conn.execute("insert into emp values(3,'Sagar',27);")
conn.execute("insert into emp values(4,'Piyush',27);")

data=conn.execute("select * from emp")

for row in data:
    print(row[0],row[1],row[2])

conn.close()