# 70. Create a function for addition of two numbers. Create a validation that both of them must be either float or integer using a built in method.

def add(x,y):
    return x+y


number1=10.58
number2=15

if isinstance(number1, (int)) and isinstance(number2, (int)):
    print("addition: ", add(number1, number2))
elif isinstance(number1, (float)) and isinstance(number2, (float)):
    print("addition: ", add(number1, number2))

else:
    print("enter both value either float or integer")




