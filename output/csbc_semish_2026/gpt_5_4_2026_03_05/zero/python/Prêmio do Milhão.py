import sys

data = list(map(int, sys.stdin.read().split()))
n = data[0]
s = 0
for i in range(1, n + 1):
    s += data[i]
    if s >= 1000000:
        print(i)
        break