import sys

data = sys.stdin.read().split()
if not data:
    exit()
n = int(data[0])
A, B, C, D, E, F, G = map(int, data[1:8])
S = A + B + C - D - E - F + G
print("N" if n == S else "S")