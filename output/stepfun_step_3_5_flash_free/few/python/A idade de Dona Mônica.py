import sys

data = sys.stdin.read().split()
if not data:
    exit()
M = int(data[0])
A = int(data[1])
B = int(data[2])
C = M - A - B
print(max(A, B, C))