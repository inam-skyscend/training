# 53. Create a dictionary containing all the Capital Letters 'A-Z', Small Letters 'a-z', and Digits '0-9' as keys and their ascii values as values using generators.

x={chr(x):x for x in list(range(ord("A"),ord("Z")+1))+list(range(ord("a"),ord("z")+1))+list(range(ord("0"),ord("9")+1))}
print(x)

