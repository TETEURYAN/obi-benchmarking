import sys

data = list(map(int, sys.stdin.read().split()))
e1, e2, e3, x = data

if e2 - e1 <= x:
    print(e2)
else:
    print(e3)