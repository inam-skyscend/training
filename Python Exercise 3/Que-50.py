# 50. Convert a Hexadecimal number '10' to binary, decimal and octal numbers.

x=0x10

y=bin(x)            #convert hexadecimal to binary
print(y)

print(oct(x))       #convert hexa to octal using oct()

print(int(y,2))     #convert binary to decimal using int(binary value,base) base=2

