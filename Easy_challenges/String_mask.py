
#Use the binary to capitalize the letters such that 1 is capital and 0 is lower


import sys
test_cases = ['hello 11001','world 10000','cba 111']

def Convert_with_mask(Str,mask):
    str_lst = []
    for ii in range(0,len(Str)):
        if int(mask[ii]) == 1 :
            #new_str = Str[ii].upper()
            #new_str
            str_lst.append(Str[ii].upper())
        else:
            str_lst.append(Str[ii])
    Output_str = ''.join(str_lst)
    return Output_str


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        lst = test.split(' ')
        String = lst[0]
        mask = lst[1]
        Masked_string  = Convert_with_mask(String,mask)
        print(Masked_string)

test_cases.close()

