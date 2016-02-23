## find the sum of the first 1000 primes

import sys

def isprime(arg): #is a number prime?
    if arg >= 3:
        for i in range(2,arg):
            if (arg % i) == 0:
                return False
        return True
    else:
        if arg == 2:
            return True
        else:
            return False

def sum_primes():
    Sum = 0
    Prime_count = 0
    loop = 1
    while Prime_count<1000:
        if isprime(loop):
            Sum += loop
            Prime_count += 1
        loop += 1
    return Sum

Sum = sum_primes()
<<<<<<< HEAD
sys.stdout.write(str(Sum))
=======
sys.stdout.write(str(Sum))
>>>>>>> 0a34ac4579bcdbddb2c5619982ad5472765183f7
