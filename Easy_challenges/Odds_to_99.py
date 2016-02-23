#print all odd from 1 to n

def isodd(arg): #is a number odd?
    if not arg % 2 == 0:
        return True
    else:
        return False



def count_up_execute(n):
    for ii in range(1,n):
        if isodd(ii):
            print(ii)

count_up_execute(100)