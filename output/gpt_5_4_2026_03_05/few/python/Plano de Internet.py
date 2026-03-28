import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

x = data[0]
n = data[1]
used = sum(data[2:2 + n])

print((n + 1) * x - used)