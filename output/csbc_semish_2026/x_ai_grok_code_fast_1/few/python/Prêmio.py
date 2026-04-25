import sys

input_data = sys.stdin.read().split()
P = int(input_data[0])
D = int(input_data[1])
B = int(input_data[2])
soma = P * 1 + D * 2 + B * 3
if soma >= 150:
    print('B')
elif soma >= 120:
    print('D')
elif soma >= 100:
    print('P')
else:
    print('N')