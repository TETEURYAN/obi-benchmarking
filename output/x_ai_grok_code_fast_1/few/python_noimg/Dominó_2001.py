import sys

data = sys.stdin.read().split()

idx = 0

test_num = 1

while True:
    N = int(data[idx])
    idx += 1
    if N == 0:
        break
    degrees = [0] * 7
    edges = [[] for _ in range(7)]
    for _ in range(N):
        x = int(data[idx])
        y = int(data[idx + 1])
        idx += 2
        degrees[x] += 1
        degrees[y] += 1
        edges[x].append(y)
        edges[y].append(x)
    odd_count = sum(1 for d in degrees if d % 2 == 1)
    visited = [False] * 7
    start = next((i for i in range(7) if degrees[i] > 0), -1)
    if start != -1:
        stack = [start]
        visited[start] = True
        while stack:
            u = stack.pop()
            for v in edges[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)
    connected = all(visited[i] or degrees[i] == 0 for i in range(7))
    possible = (odd_count == 0 or odd_count == 2) and connected
    print(f"Teste {test_num}")
    print("sim" if possible else "nao")
    print()
    test_num += 1