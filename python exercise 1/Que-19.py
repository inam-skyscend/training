def add(*non,**key):
    sum1=0
    for i in non:
        sum1 += i
    counter=key.values()
    sum2=sum(counter)
    return sum1+sum2


obj=add(10,54,85,500,625,56551,15,a=20,c=50,o=6225,z=8000080)
print(obj)

    


