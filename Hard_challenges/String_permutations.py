#Write a program which prints all the permutations of a string
# in alphabetical order. We consider that digits < upper case letters < lower case letters.
#  The sorting should be performed in ascending order.


import sys
test_cases = ['hat\n', 'abc\n', 'Zu6\n']
#test_cases = ['hat']

def permutation(lst): #recursively enumerate permutations of a string.
   if len(lst) == 1:
     #print(lst)
     return [lst]
   perm_list = [] # resulting list
   for Current_choice in lst:
     remaining_elements = [x for x in lst if x != Current_choice]
     #print(remaining_elements)
     Remaining_permutes = permutation(remaining_elements)# permutations of sublist
     for Permutes in Remaining_permutes:
       perm_list.append([Current_choice] + Permutes)
   return perm_list

def string_to_lst(String): #convert a string into a list
    Str_lst = []
    for ii in range(0,len(String)):
        if not String[ii] == '\n':
            Str_lst.append(String[ii])
    return Str_lst

def combine_lsts_to_string(lst): #convert a list of lists to a list of strings
    lst_out =[]
    for ii in range(len(lst)):
        lst_out.append(''.join(lst[ii]))
    return lst_out

def sort_strings(lst): #Sort the strings like the challenge wants
    Sorted_list = sorted(lst,key=None,reverse=False)
    return Sorted_list

def Combine_lst_to_string(lst):
    Comma_lst= Add_internal_commas(lst)
    Output_string = ''.join(Comma_lst)
    return Output_string

def Add_internal_commas(word_list):
    New_list = []
    for idx, word in enumerate(word_list):
        New_list.append(word)
        if not idx == len(word_list)-1:
            New_list.append(',')
    output = ''.join(New_list)
    return output

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    lst = string_to_lst(str(test))
    permutation_lst = permutation(lst)
    #print(permutation_lst)
    permutation_strings = combine_lsts_to_string(permutation_lst)
    #print(permutation_strings)
    Sorted_list = sort_strings(permutation_strings)
    #print(Sorted_list)
    Output_string = Combine_lst_to_string(Sorted_list)
    print(Output_string)

test_cases.close()