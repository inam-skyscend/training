# 1. Create a connection with PostgreSQL database from Python.
import psycopg2

conn=psycopg2.connect(host='localhost',user='inamhusain',database='inam',port=5432, password='inam2001')
print(conn)