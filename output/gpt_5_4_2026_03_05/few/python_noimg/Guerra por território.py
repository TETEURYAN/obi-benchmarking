import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
a = data[1:1 + n]

total = sum(a)
half = total // 2

s = 0
for i, x in enumerate(a, 1):
    s += x
    if s == half:
        print(i)
        break