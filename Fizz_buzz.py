#sample code to read in test cases:

import sys
#test_cases = open(sys.argv[1], 'r')
test_cases = ['3 5 10','2 7 15','1 2 35','2 4 45']

def parse_input(input_str):
    input_str = input_str.rstrip()
    input_lst = input_str.split(' ')
    return input_lst

def fizz_buzz(input_lst):
    X = int(input_lst[0])
    Y = int(input_lst[1])
    N = int(input_lst[2])
    output_lst = []
    for ii in range(1,N+1,1):
        if ii % X ==0:
            if ii % Y ==0:
                output_lst.append('FB')
            else:
                output_lst.append('F')
        elif ii % Y ==0:
            output_lst.append('B')
        else:
            output_lst.append(str(ii))
    return output_lst

def Add_internal_spaces(word_list):
    New_list = []
    for idx, word in enumerate(word_list):
        New_list.append(word)
        if not idx == len(word_list)-1:
            New_list.append(' ')
    output = ''.join(New_list)
    return output


for test in test_cases:
    if test:
        input_lst = parse_input(test)
        output_lst = fizz_buzz(input_lst)
        output_str= Add_internal_spaces(output_lst)
        print(output_str)



#test_cases.close()
