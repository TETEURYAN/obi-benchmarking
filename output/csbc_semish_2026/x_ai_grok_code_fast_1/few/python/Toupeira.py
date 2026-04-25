import sys

input_data = sys.stdin.read().split()
idx = 0

S = int(input_data[idx])
T = int(input_data[idx + 1])
idx += 2

adj = [set() for _ in range(S + 1)]
for _ in range(T):
    X = int(input_data[idx])
    Y = int(input_data[idx + 1])
    adj[X].add(Y)
    adj[Y].add(X)
    idx += 2

P = int(input_data[idx])
idx += 1

count = 0
for _ in range(P):
    N = int(input_data[idx])
    idx += 1
    path = [int(input_data[idx + i]) for i in range(N)]
    idx += N
    possible = True
    for i in range(N - 1):
        if path[i + 1] not in adj[path[i]]:
            possible = False
            break
    if possible:
        count += 1

print(count)