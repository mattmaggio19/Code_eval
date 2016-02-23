#Sample code to read in test cases:

import sys
#test_cases = open(sys.argv[1], 'r')
test_cases = ['13,8','17,16','2004,4','2149,256','1912,16']

for test in test_cases:
    # ignore test if it is an empty line
    if test:
        inputs = test.split(',')
        x = int(inputs[0])
        n = int(inputs[1])
        current_num = n
        loop = 1
        while current_num < x:
            current_num = current_num * loop
            loop += 1
        sys.stdout.write(str(current_num))
        sys.stdout.write('\n')

#test_cases.close()
