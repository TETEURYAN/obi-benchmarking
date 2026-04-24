import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

p = int(input_data[0])
d1 = int(input_data[1])
d2 = int(input_data[2])

if (d1 + d2) % 2 == 0:
    print(p)
else:
    print(1 - p)