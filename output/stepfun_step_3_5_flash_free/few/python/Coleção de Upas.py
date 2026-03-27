import sys

data = sys.stdin.read().split()
if not data:
    exit()
n = int(data[0])
m = int(data[1])
adj = [[] for _ in range(n+1)]
idx = 2
for _ in range(m):
    u = int(data[idx]); v = int(data[idx+1]); idx += 2
    adj[u].append(v)
    adj[v].append(u)

forbidden = [False] * (n+1)
result = []
for i in range(n, 0, -1):
    if not forbidden[i]:
        result.append(i)
        for v in adj[i]:
            forbidden[v] = True
result.reverse()
print(len(result))
print(' '.join(map(str, result)))