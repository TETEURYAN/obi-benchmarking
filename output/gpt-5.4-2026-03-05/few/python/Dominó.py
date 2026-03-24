import sys

data = sys.stdin.read().split()
if data:
    n = int(data[0])
    print((n + 1) * (n + 2) // 2)