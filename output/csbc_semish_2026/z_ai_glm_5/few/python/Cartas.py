
import sys

data = sys.stdin.read().split()
A = int(data[0])
B = int(data[1])
C = int(data[2])

if A == B:
    print(C)
elif A == C:
    print(B)
else:
    print(A)
