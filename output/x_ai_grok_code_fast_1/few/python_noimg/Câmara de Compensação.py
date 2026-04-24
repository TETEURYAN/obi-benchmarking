import sys

data = sys.stdin.read().split()
M = int(data[0])
N = int(data[1])
saldo = [0] * (N + 1)
total = 0
idx = 2
for _ in range(M):
    X = int(data[idx])
    V = int(data[idx + 1])
    Y = int(data[idx + 2])
    saldo[Y] += V
    saldo[X] -= V
    total += V
    idx += 3
soma_pos = sum(max(0, s) for s in saldo[1:])
if total > soma_pos:
    print('S')
else:
    print('N')
print(soma_pos)