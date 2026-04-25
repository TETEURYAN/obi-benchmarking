import sys

input_data = sys.stdin.read().split()
E = int(input_data[0])
D = int(input_data[1])

if E > D:
    result = E + D
else:
    result = 2 * (D - E)

print(result)