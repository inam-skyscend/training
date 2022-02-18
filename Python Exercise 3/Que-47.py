# 47. Create a generator method to have the prime numbers using yield between 1 to 100.

def prime_generator():
    for n in range(1,100):     # n starts from 2 to 100
        for x in range(2, n):   # check if x can be divided by n
            if n % x == 0:      # if true then n is not prime
                break
        else:                   # if x is found after exhausting all values of x
            yield n             # generate the prime


g = prime_generator()
print(tuple(g))









