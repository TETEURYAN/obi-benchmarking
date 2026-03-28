import sys

data = list(map(int, sys.stdin.read().split()))
m, a, b = data[0], data[1], data[2]
c = m - a - b
print(max(a, b, c))