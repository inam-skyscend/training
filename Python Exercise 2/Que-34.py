import string
ke=[]
val=list(range(1,27))

for letter in string.ascii_lowercase:
    ke.append(letter)


print(dict(zip(ke,val)))



