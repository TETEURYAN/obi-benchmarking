import sys

a, b, c, d = map(int, sys.stdin.read().split())
if a == c or b == d:
    print('V')
else:
    print('F')