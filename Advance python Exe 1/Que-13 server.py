import socket

s = socket.socket()
print("socket created")

s.bind(('localhost',9999))

s.listen(3)
print("waiting for connections")

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    return a/b

while True:
    conn, addr = s.accept()
    print("Connected by ", addr)
    data = conn.recv(1024)
    print(conn)
    if data:
        print("Data Received", data)
        dt = data.decode('utf-8')
        print("DT", dt)
        d = dt.split(",")
        print("Data Received string", d)
        data_add = add(int(d[0]), int(d[1]))


        data_sub = sub(int(d[0]), int(d[1]))


        data_multi = multi(int(d[0]), int(d[1]))


        data_div = div(int(d[0]), int(d[1]))

        conn.send(str(data_add).encode('utf-8'))
        conn.send(str(data_sub).encode('utf-8'))
        conn.send(str(data_multi).encode('utf-8'))
        conn.send(str(data_div).encode('utf-8'))