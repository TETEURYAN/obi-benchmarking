import sys

data = sys.stdin.read().split()
if data:
    c, n = map(int, data)
    print(c % n)