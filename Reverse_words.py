



#Sample code to read in test cases:
import sys
test_cases = open(sys.argv[1], 'r')
#test_cases = ['VebReiSVOdCEjJq IdfPk8c']
def Remove_trailing_spaces(line):
    line = line.rstrip()
    return line

def Parse_input(line):
    word_list = line.split(' ')
    word_list.reverse()
    return word_list

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
        test = Remove_trailing_spaces(test)
        Reverse_words= Parse_input(test)
        Output_str = Add_internal_spaces(Reverse_words)
        sys.stdout.write(str(Output_str))
        sys.stdout.write('\n')


test_cases.close()


