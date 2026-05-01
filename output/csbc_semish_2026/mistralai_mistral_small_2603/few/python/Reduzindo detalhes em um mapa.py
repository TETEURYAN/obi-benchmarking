import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])
    edges = []
    index = 2

    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        c = int(data[index+2])
        edges.append((c, u, v))
        index += 3

    parent = [i for i in range(n+1)]
    rank = [0] * (n+1)

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

    edges.sort()
    total = 0
    for c, u, v in edges:
        if union(u, v):
            total += c

    print(total)

if __name__ == "__main__":
    main()