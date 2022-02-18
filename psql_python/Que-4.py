import psycopg2

conn=psycopg2.connect(host='localhost',user='inamhusain',database='inam',port=5432, password='inam2001')
print(conn)

cr=conn.cursor()

cr.execute('create table category (id integer PRIMARY KEY,code integer,name varchar(10))')
cr.execute('alter table category alter column name set not null;')
cr.execute('alter table category add constraint unique_code_cat unique(code)')
insert_cat = cr.execute("insert into category(id,code,name)VALUES(1,1001,'cat1'),(2,1002,'cat2'),(3,1003,'cat3'),(4,1004,'cat4')")
conn.commit()
cr.close()
conn.close()

