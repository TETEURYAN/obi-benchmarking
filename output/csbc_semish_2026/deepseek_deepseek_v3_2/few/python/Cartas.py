import sys

data = sys.stdin.read().strip().split()
if not data:
    exit()
a, b, c = map(int, data[:3])

if a == b:
    print(c)
elif a == c:
    print(b)
else:
    print(a)