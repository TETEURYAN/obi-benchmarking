import sys
sys.setrecursionlimit(200000)

def read_input():
    data = sys.stdin.read().split()
    if not data:
        return None, None, None, None
    n = int(data[0])
    m = int(data[1])
    idx = 2
    edges1 = []
    for _ in range(n - 1):
        a = int(data[idx])
        b = int(data[idx + 1])
        edges1.append((a, b))
        idx += 2
    edges2 = []
    for _ in range(m - 1):
        x = int(data[idx])
        y = int(data[idx + 1])
        edges2.append((x, y))
        idx += 2
    return n, m, edges1, edges2

def build_tree(n, edges):
    adj = [[] for _ in range(n + 1)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    return adj

def bfs(start, adj, n):
    dist = [-1] * (n + 1)
    dist[start] = 0
    queue = [start]
    farthest = start
    for node in queue:
        for neighbor in adj[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                if dist[neighbor] > dist[farthest]:
                    farthest = neighbor
                queue.append(neighbor)
    return farthest, dist

def find_diameter_ends(adj, n):
    u, _ = bfs(1, adj, n)
    v, dist = bfs(u, adj, n)
    return u, v, dist

def find_center_nodes(adj, n):
    u, v, dist = find_diameter_ends(adj, n)
    diameter_length = dist[v]
    path = []
    current = v
    while current != u:
        path.append(current)
        for neighbor in adj[current]:
            if dist[neighbor] == dist[current] - 1:
                current = neighbor
                break
    path.append(u)
    if diameter_length % 2 == 0:
        center = path[diameter_length // 2]
        return [center]
    else:
        center1 = path[diameter_length // 2]
        center2 = path[diameter_length // 2 + 1]
        return [center1, center2]

def solve():
    n, m, edges1, edges2 = read_input()
    if n is None:
        return
    adj1 = build_tree(n, edges1)
    adj2 = build_tree(m, edges2)
    centers1 = find_center_nodes(adj1, n)
    centers2 = find_center_nodes(adj2, m)
    print(centers1[0], centers2[0])

if __name__ == "__main__":
    solve()