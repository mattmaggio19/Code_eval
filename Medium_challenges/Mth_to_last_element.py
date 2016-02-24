#The first argument is a path to a file.
#The file contains the series of space delimited characters followed by an integer.
#The integer represents an index in the list (1-based), one per line.

test_cases = ['a b c d 4']


import sys

def Mth_el(string):
    lst = string.split(' ') #Create a list as a stand in for the string
    idx = int(lst[-1])
    if idx > len(lst)-1 or idx == 0:
        return False
    else:
        return str(lst[(len(lst)-1) - idx])

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        Output = Mth_el(test)
        if not Output:
           pass
        else:
            print(Output)


test_cases.close()