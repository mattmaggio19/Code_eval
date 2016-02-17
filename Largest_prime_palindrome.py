
#find the largest Prime that is also palindromic and below the number N
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
def ispalindrome(arg): #is a number a palindrome?
    Forward = str(arg)
    count = 0
    Reverse = [];
    for ii in range(len(Forward),0,-1):
        Reverse.append(Forward[ii-1])
        count += 1
    Reverse_str = ''.join(Reverse)
    if Forward == Reverse_str:
        return True
    else:
        return False


def count_down_execute(n):

    for ii in range(n,0,-1):
        if isprime(ii):
            if ispalindrome(ii):
                return ii


Largest_prime_pal = count_down_execute(1000)
sys.stdout.write(str(Largest_prime_pal))