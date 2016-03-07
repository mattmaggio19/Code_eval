#You are given two sequences. Write a program to determine the longest common subsequence between the two
# strings (each string can have a maximum length of 50 characters). NOTE: This subsequence need not be
# contiguous. The input file may contain empty lines, these need to be ignored.

#The first argument will be a path to a filename that contains two strings per line, semicolon delimited.
# You can assume that there is only one unique subsequence per test case.

test_cases = ['XMJYAUZ;MZJAWXU']

#import sys
#test_cases = open(sys.argv[1], 'r')

def find_LCS(arg1,arg2):
    print(arg1)
    print(arg2)
    LCS = ['']



for test in test_cases:
    if test:
        lst = test.split(';')
        LCS=find_LCS(lst[0],lst[1])
        print(LCS)

#test_cases.close()