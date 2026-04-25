import sys

data = sys.stdin.read().split()
if not data:
    exit()

n1, d1, v1, n2, d2, v2 = map(int, data)

if d1 * v2 < d2 * v1:
    print(n1)
else:
    print(n2)