import socket

c = socket.socket()

c.connect(("localhost",9999))

a = input('Enter first number: ')
b = input('Enter second number: ')
c = a+','+b
print(c)

print("Sending string {0} to server" .format(c))

s = socket.socket()
s.connect(("localhost",9999))

s.send(c.encode('utf-8'))
data = s.recv(1024)
data1 = s.recv(1024)
data2 = s.recv(1024)
data3 = s.recv(1024)
print(int(data.decode('utf-8')))
print(int(data1.decode('utf-8')))
print(int(data2.decode('utf-8')))
print(float(data3.decode('utf-8')))


s.close()

