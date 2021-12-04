import sqlite3

conn=sqlite3.connect("entries.db")

# conn.execute("create table records(id integer primary key autoincrement,subject string not null,teacher string not null,desc string not null,time string not null);")

conn.execute('insert into records(subject,teacher,desc,time) values("Artificial Intelligience","Meghana Lokhande","Going to learn BFS Algorithm","10:00 AM");')

conn.commit()

data=conn.execute("select * from records")

for row in data:
    print(row[0],row[1],row[2],row[3],row[4])
print("table")

conn.close()
