import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n, x1, y1, x2, y2 = data

half = n // 2

ok = (x1 <= half < x2) or (x2 <= half < x1) or (y1 <= half < y2) or (y2 <= half < y1)

print('S' if ok else 'N')