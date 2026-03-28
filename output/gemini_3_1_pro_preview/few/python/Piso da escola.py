import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

L = int(input_data[0])
C = int(input_data[1])

type1 = L * C + (L - 1) * (C - 1)
type2 = 2 * (L - 1) + 2 * (C - 1)

print(type1)
print(type2)