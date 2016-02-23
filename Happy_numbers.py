#Determine if input is happy. If yes print one on each line.
import sys
test_cases = open(sys.argv[1], 'r')
#test_cases = ["293", "760"]
for test in test_cases:
    def Happy_numbers(n):
        n_old = n
        loop = 0
        while loop < 100:
            n_string = str(n_old)
            n_new = 0
            for ii in range(0,len(n_string)):
                n_new += (int(n_string[ii]))*(int(n_string[ii]))
            n_old = n_new
            if n_old == 1:
                return True
            if n_old == n:
                return False
            loop += 1
        return False
    test = test.rstrip()
    res = Happy_numbers(test)
    if res:
        print("1")
    else:
        print("0")

test_cases.close()


