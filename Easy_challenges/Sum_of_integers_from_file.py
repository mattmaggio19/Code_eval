
#SUM OF INTEGERS FROM FILE Exactly what it sounds like

#sample code to read in test cases:

import sys
test_cases = open(sys.argv[1], 'r')
#test_cases = [3,5,8,4,9,7,10,8,1,6,6,2,1,3,7,6,8,7,7,7]
sum = 0
for test in test_cases:
    if test:
        sum = sum + int(test)
print(sum)
test_cases.close()
