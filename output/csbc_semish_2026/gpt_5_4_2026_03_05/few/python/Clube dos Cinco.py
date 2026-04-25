import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
a, b, c, d, e, f, g = data[1:8]

x = a + b + c - d - e - f + g - n

print("S" if x > 0 else "N")