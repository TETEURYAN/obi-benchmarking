import sys
from heapq import heappop, heappush

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it)
        c = int(next(it))
        edges.append((u, v, c))
    
    parent = [i for i in range(n+1)]
    rank = [0] * (n+1)
    
    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u
    
    def union(u, v, c):
        u_root = find(u)
        v_root = find(v)
        if u_root == v_root:
            return False
        if rank[u_root] < rank[v_root]:
            parent[u_root] = v_root
        elif rank[u_root] > rank[v_root]:
            parent[v_root] = u_root
        else:
            parent[v_root] = u_root
            rank[u_root] += 1
        return True
    
    edges.sort(key=lambda x: x[2])
    total = 0
    count = 0
    for u, v, c in edges:
        if union(u, v, c):
            total += c
            count += 1
            if count == n - 1:
                break
    
    print(total)

if __name__ == '__main__':
    main()