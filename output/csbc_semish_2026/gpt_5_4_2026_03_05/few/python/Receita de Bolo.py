import sys

data = sys.stdin.read().split()
a, b, c = map(int, data)
print(min(a // 2, b // 3, c // 5))