import sys

data = sys.stdin.read().split()
if not data:
    exit()

n = int(data[0])

zero = max(n - 2, 0) ** 3
one = 6 * max(n - 2, 0) ** 2
two = 12 * max(n - 2, 0)
three = 8

print(zero)
print(one)
print(two)
print(three)