import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

m = int(input_data[0])
a = int(input_data[1])
b = int(input_data[2])

c = m - a - b

print(max(a, b, c))