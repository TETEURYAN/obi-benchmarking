
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    N = int(data[idx])
    F = int(data[idx+1])
    R = int(data[idx+2])
    idx += 3

    edges = []
    for _ in range(F):
        a = int(data[idx])
        b = int(data[idx+1])
        c = int(data[idx+2])
        edges.append((c, a, b, 'F'))
        idx += 3

    for _ in range(R):
        i = int(data[idx])
        j = int(data[idx+1])
        k = int(data[idx+2])
        edges.append((k, i, j, 'R'))
        idx += 3

    edges.sort()

    parent = [i for i in range(N+1)]
    rank = [0] * (N+1)

    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u

    def union(u, v):
        u_root = find(u)
        v_root = find(v)
        if u_root == v_root:
            return False
        if rank[u_root] > rank[v_root]:
            parent[v_root] = u_root
        else:
            parent[u_root] = v_root
            if rank[u_root] == rank[v_root]:
                rank[v_root] += 1
        return True

    total_cost = 0
    count = 0
    for edge in edges:
        cost, u, v, typ = edge
        if union(u, v):
            total_cost += cost
            count += 1
            if count == N - 1:
                break

    print(total_cost)

if __name__ == "__main__":
    main()
