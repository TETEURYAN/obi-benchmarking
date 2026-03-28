import sys
from fractions import Fraction

input_data = sys.stdin.read().split()
N = int(input_data[0])
result = Fraction(1)
idx = 1
for _ in range(N):
    digit = int(input_data[idx])
    op = input_data[idx + 1]
    if op == '*':
        result *= digit
    else:
        result /= digit
    idx += 2
print(int(result))