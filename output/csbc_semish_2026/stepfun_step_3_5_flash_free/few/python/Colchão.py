import sys

data = sys.stdin.read().split()
if not data:
    exit()

A = int(data[0])
B = int(data[1])
C = int(data[2])
H = int(data[3])
L = int(data[4])

if (A <= H and min(B, C) <= L) or (B <= H and min(A, C) <= L) or (C <= H and min(A, B) <= L):
    print('S')
else:
    print('N')