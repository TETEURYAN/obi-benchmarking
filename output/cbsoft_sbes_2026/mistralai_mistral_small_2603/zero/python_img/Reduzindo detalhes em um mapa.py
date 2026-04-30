
import sys

def main():
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr])
    ptr += 1
    M = int(input[ptr])
    ptr += 1

    edges = []
    for _ in range(M):
        u = int(input[ptr])
        ptr += 1
        v = int(input[ptr])
        ptr += 1
        c = int(input[ptr])
        ptr += 1
        edges.append((c, u, v))

    edges.sort()

    parent = [i for i in range(N + 1)]
    rank = [0] * (N + 1)

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

    total = 0
    for c, u, v in edges:
        if union(u, v):
            total += c

    print(total)

if __name__ == "__main__":
    main()
