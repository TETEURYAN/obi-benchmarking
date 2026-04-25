import sys

a, b, c, d = map(int, sys.stdin.read().split())

if a == b + c + d and b + c == d and b == c:
    print("S")
else:
    print("N")