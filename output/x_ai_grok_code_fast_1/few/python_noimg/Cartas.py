import sys

input_data = sys.stdin.read().split()
A = int(input_data[0])
B = int(input_data[1])
C = int(input_data[2])

if A == B:
    print(C)
elif A == C:
    print(B)
else:
    print(A)