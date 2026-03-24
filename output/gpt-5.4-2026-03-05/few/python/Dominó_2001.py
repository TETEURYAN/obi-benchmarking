import sys

data = sys.stdin.read().split()
out = []
i = 0
teste = 1

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
        deg[x] += 1
        deg[y] += 1
        adj[x][y] += 1
        if x != y:
            adj[y][x] += 1

    vertices = [v for v in range(7) if deg[v] > 0]

    possible = True

    odd = sum(1 for v in range(7) if deg[v] % 2 == 1)
    if odd != 0 and odd != 2:
        possible = False

    if possible and vertices:
        start = vertices[0]
        stack = [start]
        vis = [False] * 7
        vis[start] = True

        while stack:
            u = stack.pop()
            for v in range(7):
                if adj[u][v] > 0 and not vis[v]:
                    vis[v] = True
                    stack.append(v)

        for v in vertices:
            if not vis[v]:
                possible = False
                break

    out.append(f"Teste {teste}")
    out.append("sim" if possible else "nao")
    out.append("")
    teste += 1

sys.stdout.write("\n".join(out))