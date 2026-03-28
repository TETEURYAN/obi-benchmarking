import sys

input_data = sys.stdin.read().split()
A = int(input_data[0])
B = int(input_data[1])
R = int(input_data[2])
G = int(input_data[3])

if A >= 2 * R and B >= 2 * R and 360 % G == 0:
    print('S')
else:
    print('N')