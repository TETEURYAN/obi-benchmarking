import sys

data = sys.stdin.read().split()
idx = 0
A = int(data[idx]); idx += 1
B = int(data[idx]); idx += 1
SA = data[idx:idx+A]; idx += A
SB = data[idx:idx+B]

j = 0
for i in range(A):
    if j < B and SA[i] == SB[j]:
        j += 1

print('S' if j == B else 'N')