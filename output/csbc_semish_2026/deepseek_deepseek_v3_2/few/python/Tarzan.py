import sys

def dist(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return dx*dx + dy*dy

def dfs(u, visited, adj):
    visited[u] = True
    for v in adj[u]:
        if not visited[v]:
            dfs(v, visited, adj)

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    D = int(next(it))
    points = []
    for _ in range(N):
        x = int(next(it))
        y = int(next(it))
        points.append((x, y))

    adj = [[] for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            d2 = dist(points[i], points[j])
            if d2 <= D*D:
                adj[i].append(j)
                adj[j].append(i)

    visited = [False] * N
    dfs(0, visited, adj)

    if all(visited):
        print('S')
    else:
        print('N')

if __name__ == "__main__":
    main()