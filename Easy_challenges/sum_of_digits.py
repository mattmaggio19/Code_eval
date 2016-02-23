#output the sum of the digits in a number
import sys
test_cases = open(sys.argv[1], 'r')
#test_cases = ["293", "760"]
for test in test_cases:
    def Sum_of_digits(n):
        n_string = str(n)
        n_new = 0
        for ii in range(0,len(n_string)):
                n_new += (int(n_string[ii]))
        else:
            print(n_new)

    test = test.rstrip()
    Sum_of_digits(test)

test_cases.close()


