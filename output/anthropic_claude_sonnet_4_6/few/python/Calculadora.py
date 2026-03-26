import sys
from fractions import Fraction

data = sys.stdin.read().split()
n = int(data[0])
result = Fraction(1)
idx = 1
for _ in range(n):
    num = int(data[idx])
    op = data[idx+1]
    idx += 2
    if op == '*':
        result *= num
    else:
        result /= num

print(int(result))