import psycopg2

conn=psycopg2.connect(host='localhost',user='inamhusain',database='inam',port=5432, password='inam2001')
print(conn)

cr=conn.cursor()
cr.execute('select pr.id,pr.name,pr.cost_price,pr.sale_price,ct.code,ct.name from product pr full join category ct on pr.id=ct.id;')
i=cr.fetchall()
print(i)

cr.close()
conn.close()