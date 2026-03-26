import sys
a, b, c = map(int, sys.stdin.read().split())
vals = sorted([a, b, c])
print(vals[1])