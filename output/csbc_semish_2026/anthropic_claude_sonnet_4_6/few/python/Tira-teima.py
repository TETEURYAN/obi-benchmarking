import sys
x, y = map(int, sys.stdin.read().split())
if 0 <= x <= 432 and 0 <= y <= 468:
    print("dentro")
else:
    print("fora")