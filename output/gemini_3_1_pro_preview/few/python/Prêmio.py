import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

p = int(input_data[0])
d = int(input_data[1])
b = int(input_data[2])

total = p * 1 + d * 2 + b * 3

if total >= 150:
    print('B')
elif total >= 120:
    print('D')
elif total >= 100:
    print('P')
else:
    print('N')