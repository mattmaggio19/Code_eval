#print multiplication tables up to n x n


def Line_generate(line_num,row_num): #Generate each line
    Line_lst = []
    for ii in range(1,row_num+1):
        Line_lst.append(line_num*ii)
    return Line_lst

def Generate_tables(n):
    for ii in range(1,n+1):
        Line_lst = Line_generate(ii,n)
        Line_lst_spaces =Add_spaces(Line_lst)
        Output_line = ''.join(Line_lst_spaces)
        print(Output_line)

def Add_spaces(lst):
    output_lst = []
    Total_space_for_entry = 4
    for ii in range(0,len(lst)):
        num_as_str = str(lst[ii])
        output_lst.append(num_as_str)
        if not ii == len(lst)-1:
            for jj in range(Total_space_for_entry - len(str(lst[ii+1]))):
                output_lst.append(' ')
    return output_lst


Generate_tables(12)