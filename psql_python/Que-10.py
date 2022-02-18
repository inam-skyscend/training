import psycopg2

conn=psycopg2.connect(host='localhost',user='inamhusain',database='inam',port=5432, password='inam2001')
print(conn)

cr=conn.cursor()
select_all = cr.execute("select max(sale_price) from product")
print(select_all)

fetch_all_data = cr.fetchall()
print(fetch_all_data)