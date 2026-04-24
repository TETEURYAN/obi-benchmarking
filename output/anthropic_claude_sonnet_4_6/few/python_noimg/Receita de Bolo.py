import sys
a, b, c = map(int, sys.stdin.read().split())
print(min(a // 2, b // 3, c // 5))