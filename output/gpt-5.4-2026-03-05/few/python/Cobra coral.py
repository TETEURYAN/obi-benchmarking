import sys

a = list(map(int, sys.stdin.read().split()))
x1, x2, x3, x4 = a

if x1 == x3:
    print("V")
else:
    print("F")