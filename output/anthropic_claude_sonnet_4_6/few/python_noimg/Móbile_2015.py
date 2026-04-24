import sys
data = sys.stdin.read().split()
A, B, C, D = int(data[0]), int(data[1]), int(data[2]), int(data[3])
if A == B + C + D and B + C == D and B == C:
    print("S")
else:
    print("N")