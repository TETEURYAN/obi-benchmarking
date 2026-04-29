import sys

vals = list(map(int, sys.stdin.read().split()))
A, B, C, D = vals[:4]

if A == B + C + D and B + C == D and B == C:
    print("S")
else:
    print("N")