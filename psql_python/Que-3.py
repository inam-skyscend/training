import psycopg2

conn=psycopg2.connect(host='localhost',user='inamhusain',database='inam',port=5432, password='inam2001')
print(conn)

cr=conn.cursor()
print(cr)

cr.execute('create table product (id integer PRIMARY KEY, name varchar(10),cost_price integer,sale_price integer)')
cr.execute('create sequence seq_id increment 1 start with 101')
cr.execute('alter table product add constraint check_price check(cost_price < sale_price)')
insert = cr.execute("insert into product(id,cost_price,sale_price)VALUES(nextval('seq_id'),300,500),(nextval('seq_id'),300,600),(nextval('seq_id'),400,500)")
conn.commit()
conn.close()
cr.close()
