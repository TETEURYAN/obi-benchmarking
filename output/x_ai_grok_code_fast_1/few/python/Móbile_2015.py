import sys

input_data = sys.stdin.read().split()

A = int(input_data[0])
B = int(input_data[1])
C = int(input_data[2])
D = int(input_data[3])

if A == B + C + D and B + C == D and B == C:
    print("S")
else:
    print("N")