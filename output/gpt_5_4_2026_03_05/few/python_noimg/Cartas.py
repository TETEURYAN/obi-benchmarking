import sys

data = sys.stdin.read().split()
a, b, c = map(int, data[:3])

if a == b:
    print(c)
elif a == c:
    print(b)
else:
    print(a)