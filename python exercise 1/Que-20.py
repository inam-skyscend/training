def pwr(no, Power=0):

    if Power ==0:
        return no**Power
    elif Power == 1:
        return no

    else:
        return (no * pwr(no, Power-1))




k=pwr(5,pwr(2,pwr(2,2)))
print(k)


