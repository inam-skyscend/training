# 5. Add a foreign key for category in product table.
import psycopg2

conn=psycopg2.connect(host='localhost',user='inamhusain',database='inam',port=5432, password='inam2001')
print(conn)

cr=conn.cursor()
cr.execute("alter table product add column cat_id integer")
cr.execute("alter table product add constraint fk_cat foreign key(cat_id) references category(id)")

conn.commit()

