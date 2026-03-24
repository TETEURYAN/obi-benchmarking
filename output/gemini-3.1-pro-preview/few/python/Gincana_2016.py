import sys
import math

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
m = int(input_data[1])

for x in range(m, 0, -1):
    if math.gcd(n, x) == 1:
        print(x)
        break