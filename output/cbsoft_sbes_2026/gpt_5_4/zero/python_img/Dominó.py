import sys

data = sys.stdin.read().strip().split()
i = 0
teste = 1
out = []

while i < len(data):
    n = int(data[i])
    i += 1
    if n == 0:
        break

    deg = [0] * 7
    adj = [[0] * 7 for _ in range(7)]

    for _ in range(n):
        x = int(data[i])
        y = int(data[i + 1])
        i += 2
        if x == y:
            deg[x] += 2
        else:
            deg[x] += 1
            deg[y] += 1
        adj[x][y] += 1
        if x != y:
            adj[y][x] += 1

    odd = sum(d % 2 for d in deg)

    start = -1
    for v in range(7):
        if deg[v] > 0:
            start = v
            break

    connected = True
    if start != -1:
        vis = [False] * 7
        stack = [start]
        vis[start] = True
        while stack:
            u = stack.pop()
            for v in range(7):
                if adj[u][v] > 0 and not vis[v]:
                    vis[v] = True
                    stack.append(v)
        for v in range(7):
            if deg[v] > 0 and not vis[v]:
                connected = False
                break

    possible = connected and (odd == 0 or odd == 2)

    out.append(f"Teste {teste}")
    out.append("sim" if possible else "nao")
    out.append("")
    teste += 1

sys.stdout.write("\n".join(out))