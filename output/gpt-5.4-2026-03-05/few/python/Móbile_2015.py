import sys

data = list(map(int, sys.stdin.read().split()))
a, b, c, d = data

if a == b + c + d and b + c == d and b == c:
    print("S")
else:
    print("N")