import sys

data = sys.stdin.read().split()
idx = 0
S = int(data[idx])
idx += 1
T = int(data[idx])
idx += 1
adj = [[False] * (S + 1) for _ in range(S + 1)]
for _ in range(T):
    X = int(data[idx])
    idx += 1
    Y = int(data[idx])
    idx += 1
    adj[X][Y] = True
    adj[Y][X] = True
P = int(data[idx])
idx += 1
count = 0
for _ in range(P):
    N = int(data[idx])
    idx += 1
    C = [int(data[idx + i]) for i in range(N)]
    idx += N
    valid = True
    for i in range(N - 1):
        if not adj[C[i]][C[i + 1]]:
            valid = False
            break
    if valid:
        count += 1
print(count)