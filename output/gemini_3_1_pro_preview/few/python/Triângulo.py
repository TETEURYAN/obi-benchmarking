import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

v = sorted([int(x) for x in input_data])

if v[0] + v[1] > v[2] or v[1] + v[2] > v[3]:
    print('S')
else:
    print('N')