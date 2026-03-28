import sys
sys.setrecursionlimit(200000)

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    E = int(next(it))
    I = int(next(it))
    V = int(next(it))
    
    adj = [[] for _ in range(E + 1)]
    indeg = [0] * (E + 1)
    
    for _ in range(I):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b)
        indeg[b] += 1
    
    initial_true = [False] * (E + 1)
    for _ in range(V):
        x = int(next(it))
        initial_true[x] = True
    
    # Topological order
    order = []
    stack = [i for i in range(1, E + 1) if indeg[i] == 0]
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                stack.append(v)
    
    # Forward propagation
    certain = initial_true[:]
    for u in order:
        if certain[u]:
            for v in adj[u]:
                certain[v] = True
    
    # Backward propagation
    rev_adj = [[] for _ in range(E + 1)]
    for u in range(1, E + 1):
        for v in adj[u]:
            rev_adj[v].append(u)
    
    visited = [False] * (E + 1)
    def dfs_back(node):
        if visited[node]:
            return
        visited[node] = True
        for prev in rev_adj[node]:
            if not visited[prev]:
                dfs_back(prev)
    
    for u in range(1, E + 1):
        if certain[u]:
            dfs_back(u)
    
    result = [i for i in range(1, E + 1) if visited[i]]
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()