import sys
sys.setrecursionlimit(200000)

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    adj = [[] for _ in range(n + 1)]
    idx = 1
    for _ in range(n - 1):
        u = int(data[idx])
        v = int(data[idx + 1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2

    # Encontrar os dois pontos mais distantes (extremidades do diâmetro)
    # Primeira DFS para encontrar um extremo
    dist = [-1] * (n + 1)
    stack = [(1, 0)]
    dist[1] = 0
    farthest = 1
    while stack:
        node, d = stack.pop()
        if d > dist[farthest]:
            farthest = node
        for neighbor in adj[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = d + 1
                stack.append((neighbor, d + 1))

    # Segunda DFS do extremo encontrado para encontrar o outro extremo e o diâmetro
    dist = [-1] * (n + 1)
    stack = [(farthest, 0)]
    dist[farthest] = 0
    diam_end = farthest
    diam_len = 0
    while stack:
        node, d = stack.pop()
        if d > diam_len:
            diam_len = d
            diam_end = node
        for neighbor in adj[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = d + 1
                stack.append((neighbor, d + 1))

    # O ciclo máximo é diam_len + 1 (distância entre extremos + nova aresta)
    max_cycle_len = diam_len + 1

    # Precisamos contar quantos pares de vértices (u, v) produzem esse ciclo máximo.
    # Para isso, precisamos das distâncias de todos os vértices aos dois extremos do diâmetro.
    dist_a = [-1] * (n + 1)
    dist_b = [-1] * (n + 1)

    # DFS do primeiro extremo (farthest)
    stack = [(farthest, 0)]
    dist_a[farthest] = cardinality = 0
    while stack:
        node, d = stack.pop()
        dist_a[node] = cardinality = cardinality + 1
        for neighbor in adj[node]:
            if dist_a[neighbor] == -1:
                dist_a[neighbor] = cardinality
                stack.append((neighbor, cardinality))

    # DFS do segundo extremo (diam_end)
    stack = [(diam_end, 0)]
    dist_b[diam_end] = cardinality = 0
    while stack:
        node, d = stack.pop()
        dist_b[node] = cardinality
        for neighbor in adj[node]:
            if dist_b[neighbor] == -1:
                dist_b[neighbor] = cardinality
                stack.append((neighbor, cardinality))

    # Contagem de pares que formam ciclo de tamanho máximo
    count = 0
    for u in range(1, n + 1):
        for v in range(u + 1, n + 1):
            if dist_a[u] + dist_b[v] + 1 == max_cycle_len:
                count += 1
            elif dist_a[v] + dist_b[u] + 1 == max_cycle_len:
                count += 1

    print(max_cycle_len)
    print(count)

if __name__ == "__main__":
    main()