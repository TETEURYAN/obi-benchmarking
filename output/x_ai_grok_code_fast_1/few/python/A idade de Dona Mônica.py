import sys

input_data = sys.stdin.read().split()
M = int(input_data[0])
A = int(input_data[1])
B = int(input_data[2])
C = M - A - B
print(max(A, B, C))