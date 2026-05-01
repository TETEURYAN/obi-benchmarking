import sys

input_data = sys.stdin.read().split()
X = int(input_data[0])
Y = int(input_data[1])
if -8 <= X <= 8 and 0 <= Y <= 8:
    print('S')
else:
    print('N')