#Write a program which prints all the permutations of a string
# in alphabetical order. We consider that digits < upper case letters < lower case letters.
#  The sorting should be performed in ascending order.


#import sys
test_cases = ['hat', 'abc', 'Zu6']


def calc_num_permutes(Str_lst):
    pass

def permute_string(String):
    lst_of_permutes = []
    Str_lst = []
    for ii in range(0,len(String)):
        Str_lst.append(String[ii])
    print(Str_lst)


for test in test_cases:
    lst_of_permutes = permute_string(str(test))
