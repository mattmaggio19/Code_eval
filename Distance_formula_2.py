
import sys
from math import sqrt
#Sample code to read in test cases:

test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    def Parse_input(line):
        line = line.replace(',','')
        line = line.replace('(','')
        line = line.replace(')','')
        Coords = line.split(' ')
        return Coords


    def Calculate_distance(Coords):
        X1 = int(Coords[0])
        Y1 = int(Coords[1])
        X2 = int(Coords[2])
        Y2 = int(Coords[3])
        Distance = sqrt((Y1-Y2)**2 + (X1-X2)**2)
        return Distance


    Coords= Parse_input(test)
    Distance = Calculate_distance(Coords)
    sys.stdout.write(str(int(Distance)))
    sys.stdout.write('\n')


test_cases.close()


