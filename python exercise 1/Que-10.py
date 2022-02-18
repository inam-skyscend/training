#Create a python script/program that will take input from the user for 3 numbers and result will print the biggest number and the smallest number using 'input' and 'print'

a=int(input("Enter First number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))

if a > b and a > c:
    print("Biggest number is a:", a)
elif b > c and b > a:
    print("Biggest number is b:", b)
else:
    print("Biggest number is c:", c)


if a < b and a < c:
    print("Lowest number is a:", a)
elif b < c and b < a:
    print("Lowest number is b:", b)
else:
    print("Lowest number is c:", c)

