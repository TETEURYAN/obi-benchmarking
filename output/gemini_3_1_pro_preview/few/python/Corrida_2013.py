import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n1 = int(input_data[0])
d1 = int(input_data[1])
v1 = int(input_data[2])

n2 = int(input_data[3])
d2 = int(input_data[4])
v2 = int(input_data[5])

if d1 * v2 < d2 * v1:
    print(n1)
else:
    print(n2)