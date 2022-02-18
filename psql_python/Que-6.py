import psycopg2

conn=psycopg2.connect(host='localhost',user='inamhusain',database='inam',port=5432, password='inam2001')
print(conn)

cr=conn.cursor()
cr.execute("insert into product (id,name,cost_price,sale_price,cat_id)VALUES(1,'Bakedgoods',100,200,1),(2,'Beverages',200,300,2),(3,'Beverages',200,300,3),(4,'Nutritional Drinks',100,400,4),(5,'Biscuits',150,300,5)")

conn.commit()