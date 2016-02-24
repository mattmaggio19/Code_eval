#Your program should accept a path to a file as its first argument.
#The file contains multiple lines. The first line indicates the number of lines you should output,
#the other lines are of different length and are presented randomly. You may assume that the input
#file is formatted correctly and the number in the first line is a valid positive integer.

#test_cases = ['2','Hello World','CodeEval','Quick Fox','A','San Francisco']
import sys
test_cases = open(sys.argv[1], 'r')

def Compile_lst_of_lens(lst):
    len_lst = []
    for item in lst:
        len_lst.append(len(item))
    return len_lst

lst = []
for test in test_cases:
    lst.append(test)

num_to_print = int(lst[0])
lst.remove(lst[0])
len_lst = Compile_lst_of_lens(lst)

for prints in range(num_to_print):
    idx = len_lst.index((max(len_lst)))
    print(lst[idx])
    len_lst[idx]= 0

test_cases.close()