import sys

data = sys.stdin.read().split()
if not data:
    exit()

n = int(data[0])

zero = (n - 2) ** 3
one = 6 * (n - 2) ** 2
two = 12 * (n - 2)
three = 8

print(zero)
print(one)
print(two)
print(three)