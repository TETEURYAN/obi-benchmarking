
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    idx = 0
    N = int(data[idx])
    M = int(data[idx+1])
    idx += 2

    adj_circle = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a = int(data[idx])
        b = int(data[idx+1])
        adj_circle[a].append(b)
        adj_circle[b].append(a)
        idx += 2

    adj_square = [[] for _ in range(M+1)]
    for _ in range(M-1):
        x = int(data[idx])
        y = int(data[idx+1])
        adj_square[x].append(y)
        adj_square[y].append(x)
        idx += 2

    def bfs(start, adj, n):
        dist = [-1] * (n+1)
        q = deque()
        q.append(start)
        dist[start] = 0
        while q:
            u = q.popleft()
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
        return dist

    def get_diameter(adj, n):
        dist1 = bfs(1, adj, n)
        u = dist1.index(max(dist1))
        dist2 = bfs(u, adj, n)
        v = dist2.index(max(dist2))
        diameter = dist2[v]
        return u, v, diameter

    u_c, v_c, d_c = get_diameter(adj_circle, N)
    u_s, v_s, d_s = get_diameter(adj_square, M)

    dist_circle_u = bfs(u_c, adj_circle, N)
    dist_circle_v = bfs(v_c, adj_circle, N)
    dist_square_u = bfs(u_s, adj_square, M)
    dist_square_v = bfs(v_s, adj_square, M)

    best = float('inf')
    best_pair = (1, 1)

    for i in range(1, N+1):
        d1 = dist_circle_u[i]
        d2 = dist_circle_v[i]
        radius_circle = max(d1, d2)
        for j in range(1, M+1):
            d3 = dist_square_u[j]
            d4 = dist_square_v[j]
            radius_square = max(d3, d4)
            total_radius = max(radius_circle, radius_square, (d_c + 1) // 2 + (d_s + 1) // 2 + 1)
            if total_radius < best:
                best = total_radius
                best_pair = (i, j)

    print(f"{best_pair[0]} {best_pair[1]}")

if __name__ == "__main__":
    main()
