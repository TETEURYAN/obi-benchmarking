import sys

data = sys.stdin.read().split()
a, b, c, d = map(int, data[:4])

if a == b + c + d and b + c == d and b == c:
    print("S")
else:
    print("N")