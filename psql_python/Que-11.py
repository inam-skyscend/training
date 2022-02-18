import psycopg2

conn=psycopg2.connect(host='localhost',user='inamhusain',database='inam',port=5432, password='inam2001')
print(conn)

cr=conn.cursor()


cr.execute("update product set cost_price = 100 where id = 4")
cr.execute("update product set cost_price = 300 where id = 3")
cr.execute("update product set cost_price = 80 where id = 5")

select_all_cat = cr.execute("select * from product")
print(select_all_cat)

fetch_all_data = cr.fetchall()
print(fetch_all_data)
