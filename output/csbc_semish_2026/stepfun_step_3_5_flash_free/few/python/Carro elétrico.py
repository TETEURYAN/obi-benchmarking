import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    X = int(next(it)); Y = int(next(it))
    N = int(next(it)); A = int(next(it))
    xs = [0]*N
    ys = [0]*N
    for i in range(N):
        xs[i] = int(next(it))
        ys[i] = int(next(it))
    
    parent = list(range(N))
    rank = [0]*N
    
    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u
    
    def union(u, v):
        ru = find(u)
        rv = find(v)
        if ru == rv:
            return
        if rank[ru] < rank[rv]:
            parent[ru] = rv
        elif rank[ru] > rank[rv]:
            parent[rv] = ru
        else:
            parent[rv] = ru
            rank[ru] += 1
    
    for i in range(N):
        for j in range(i+1, N):
            if 100 * (abs(xs[i]-xs[j]) + abs(ys[i]-ys[j])) <= A:
                union(i, j)
    
    comps = set()
    for i in range(N):
        comps.add(find(i))
    print(len(comps)-1)

if __name__ == "__main__":
    main()