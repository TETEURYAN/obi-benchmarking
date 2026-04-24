import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

p = int(input_data[0])
r = int(input_data[1])

if p == 0:
    print('C')
elif r == 0:
    print('B')
else:
    print('A')