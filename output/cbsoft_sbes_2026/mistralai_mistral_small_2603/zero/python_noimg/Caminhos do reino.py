
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    ptr = 0
    N = int(data[ptr])
    ptr += 1
    F = [0] * (N + 1)
    for i in range(1, N + 1):
        F[i] = int(data[ptr])
        ptr += 1
    Q = int(data[ptr])
    ptr += 1
    queries = []
    for _ in range(Q):
        A = int(data[ptr])
        B = int(data[ptr + 1])
        queries.append((A, B))
        ptr += 2

    visited = [False] * (N + 1)
    in_cycle = [False] * (N + 1)
    cycle_nodes = []
    parent = [0] * (N + 1)
    depth = [0] * (N + 1)

    def find_cycle():
        for i in range(1, N + 1):
            if not visited[i]:
                stack = []
                current = i
                while True:
                    if visited[current]:
                        if current in stack:
                            idx = stack.index(current)
                            cycle_nodes.extend(stack[idx:])
                        break
                    visited[current] = True
                    stack.append(current)
                    current = F[current]
        return cycle_nodes

    cycle_nodes = find_cycle()
    cycle_set = set(cycle_nodes)
    for node in cycle_nodes:
        in_cycle[node] = True

    def bfs_cycle():
        q = deque()
        for node in cycle_nodes:
            q.append(node)
            depth[node] = 0
            parent[node] = -1

        while q:
            u = q.popleft()
            for v in range(1, N + 1):
                if F[v] == u:
                    if not in_cycle[v]:
                        in_cycle[v] = True
                        depth[v] = depth[u] + 1
                        parent[v] = u
                        q.append(v)

    bfs_cycle()

    def lca(u, v):
        while u != v:
            if depth[u] > depth[v]:
                u = parent[u]
            else:
                v = parent[v]
        return u

    def dist_to_cycle(u):
        res = 0
        while not in_cycle[u]:
            u = F[u]
            res += 1
        return res

    def dist_in_cycle(u, v):
        if u == v:
            return 0
        path_u = []
        path_v = []
        while u != v:
            if depth[u] > depth[v]:
                path_u.append(u)
                u = parent[u]
            else:
                path_v.append(v)
                v = parent[v]
        path_u.append(u)
        path = path_u + path_v[::-1]
        min_dist = float('inf')
        for i in range(len(path)):
            for j in range(i, len(path)):
                dist = j - i
                if dist < min_dist:
                    min_dist = dist
        return min_dist

    def solve_query(a, b):
        if a == b:
            return 0
        da = dist_to_cycle(a)
        db = dist_to_cycle(b)
        l = lca(a, b)
        dl = dist_to_cycle(l)
        option1 = da + db
        option2 = da + dl + (depth[l] - depth[lca(l, b)])
        option3 = db + dl + (depth[l] - depth[lca(l, a)])
        return min(option1, option2, option3)

    for a, b in queries:
        print(solve_query(a, b))

if __name__ == "__main__":
    main()
