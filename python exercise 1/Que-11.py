#Create another script/program using 'input' and pass all the three parameters as a single input and execute the same program as mentioned above.
a,b,c=map(int,input("enter number:").split())

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

