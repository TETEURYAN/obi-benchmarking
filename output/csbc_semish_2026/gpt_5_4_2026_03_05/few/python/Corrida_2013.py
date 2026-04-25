import sys

data = list(map(int, sys.stdin.read().split()))
n1, d1, v1, n2, d2, v2 = data

if d1 * v2 < d2 * v1:
    print(n1)
else:
    print(n2)