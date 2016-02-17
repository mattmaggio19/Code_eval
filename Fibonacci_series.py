#Sample code to read in test cases:

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        def fibonacci(n):
            if n == 0:
                return 0
            elif n ==1:
                return 1
            else:
                return fibonacci(n-1)+fibonacci(n-2)

    fib_n =fibonacci(int(test))
    sys.stdout.write(str(fib_n))
    sys.stdout.write('\n')


test_cases.close()


