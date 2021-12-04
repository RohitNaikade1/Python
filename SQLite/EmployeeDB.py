import sqlite3

con=sqlite3.connect("employee.db")

print("database connected successfully")

#con.execute("create table emp(id integer primary key autoincrement,name text not null,email text unique not null,address text not null)")

data=con.execute("select * from emp")

for row in data:
    print(row[0],row[1],row[2])

print("table created")

con.close()
