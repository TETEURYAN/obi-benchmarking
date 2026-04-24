
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    idx = 0
    N = int(data[idx])
    M = int(data[idx + 1])
    idx += 2

    adj_circle = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a = int(data[idx])
        b = int(data[idx + 1])
        adj_circle[a].append(b)
        adj_circle[b].append(a)
        idx += 2

    adj_square = [[] for _ in range(M + 1)]
    for _ in range(M - 1):
        x = int(data[idx])
        y = int(data[idx + 1])
        adj_square[x].append(y)
        adj_square[y].append(x)
        idx += 2

    def bfs(start, adj, n):
        dist = [-1] * (n + 1)
        q = deque()
        q.append(start)
        dist[start] = 0
        last_node = start
        max_dist = 0
        while q:
            u = q.popleft()
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
                    if dist[v] > max_dist:
                        max_dist = dist[v]
                        last_node = v
        return last_node, max_dist, dist

    def get_diameter(adj, n):
        u, _, _ = bfs(1, adj, n)
        v, diameter, _ = bfs(u, adj, n)
        return u, v, diameter

    u_c, v_c, diameter_c = get_diameter(adj_circle, N)
    u_s, v_s, diameter_s = get_diameter(adj_square, M)

    def get_farthest_nodes(start, adj, n):
        _, _, dist = bfs(start, adj, n)
        max_dist = max(dist[1:])
        candidates = [i for i in range(1, n + 1) if dist[i] == max_dist]
        return candidates

    circle_candidates = get_farthest_nodes(u_c, adj_circle, N)
    square_candidates = get_farthest_nodes(u_s, adj_square, M)

    def get_distances_to_center(start, adj, n):
        dist = [-1] * (n + 1)
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

    center_circle_dist = get_distances_to_center(u_c, adj_circle, N)
    center_square_dist = get_distances_to_center(u_s, adj_square, M)

    min_diameter = float('inf')
    best_pair = (1, 1)

    for c in circle_candidates:
        for s in square_candidates:
            new_diameter = max(diameter_c, diameter_s, (center_circle_dist[c] + 1 + center_square_dist[s]))
            if new_diameter < min_diameter:
                min_diameter = new_diameter
                best_pair = (c, s)

    print(f"{best_pair[0]} {best_pair[1]}")

if __name__ == "__main__":
    main()
