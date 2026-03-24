import sys

data = sys.stdin.read().split()
x, y = map(int, data)

if 0 <= x <= 432 and 0 <= y <= 468:
    print("dentro")
else:
    print("fora")