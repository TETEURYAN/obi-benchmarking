import sys

data = list(map(int, sys.stdin.read().split()))
i = 0
teste = 1
out = []

while i < len(data):
    E = data[i]
    L = data[i + 1]
    i += 2

    if E == 0 and L == 0:
        break

    adj = [[] for _ in range(E + 1)]
    for _ in range(L):
        x = data[i]
        y = data[i + 1]
        i += 2
        adj[x].append(y)
        adj[y].append(x)

    visited = [False] * (E + 1)
    stack = [1]
    visited[1] = True
    count = 1

    while stack:
        u = stack.pop()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                count += 1
                stack.append(v)

    out.append(f"Teste {teste}")
    out.append("normal" if count == E else "falha")
    out.append("")
    teste += 1

sys.stdout.write("\n".join(out))