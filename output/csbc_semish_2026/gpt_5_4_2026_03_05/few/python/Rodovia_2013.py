import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])
adj = [[] for _ in range(n + 1)]
radj = [[] for _ in range(n + 1)]

idx = 1
for _ in range(n):
    a = int(data[idx])
    b = int(data[idx + 1])
    idx += 2
    adj[a].append(b)
    radj[b].append(a)

def reachable(graph):
    vis = [False] * (n + 1)
    stack = [1]
    vis[1] = True
    count = 1
    while stack:
        u = stack.pop()
        for v in graph[u]:
            if not vis[v]:
                vis[v] = True
                count += 1
                stack.append(v)
    return count == n

print('S' if reachable(adj) and reachable(radj) else 'N')