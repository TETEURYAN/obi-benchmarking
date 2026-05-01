import sys
import heapq

def solve():
    sys.setrecursionlimit(200000)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    E = int(input_data[0])
    R = int(input_data[1])
    
    adj = [[] for _ in range(E + 1)]
    idx = 2
    for _ in range(R):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        w = int(input_data[idx+2])
        adj[u].append((v, w))
        adj[v].append((u, w))
        idx += 3
        
    K = int(input_data[idx])
    idx += 1
    
    queries = []
    for _ in range(K):
        X = int(input_data[idx])
        T = int(input_data[idx+1])
        queries.append((X, T))
        idx += 2
        
    visited = [False] * (E + 1)
    parent = [0] * (E + 1)
    depth = [0] * (E + 1)
    dist_from_root = [0] * (E + 1)
    cycles = []
    
    def dfs(u, p, d, dist):
        visited[u] = True
        parent[u] = p
        depth[u] = d
        dist_from_root[u] = dist
        
        for v, w in adj[u]:
            if v == p:
                continue
            if visited[v]:
                if depth[v] < depth[u]:
                    cycle_len = dist_from_root[u] - dist_from_root[v] + w
                    cycle_nodes = []
                    curr = u
                    while curr != v:
                        cycle_nodes.append(curr)
                        curr = parent[curr]
                    cycle_nodes.append(v)
                    cycles.append((cycle_len, cycle_nodes))
            else:
                dfs(v, u, d + 1, dist + w)
                
    for i in range(1, E + 1):
        if not visited[i]:
            dfs(i, 0, 0, 0)
            
    INF = 10**15
    out = []
    for X, T in queries:
        dist = [INF] * (E + 1)
        dist[X] = 0
        pq = [(0, X)]
        
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            
            for v, w in adj[u]:
                if d + w < dist[v]:
                    dist[v] = d + w
                    heapq.heappush(pq, (dist[v], v))
                    
        ans = INF
        for cycle_len, cycle_nodes in cycles:
            if cycle_len >= T:
                min_d = INF
                for v in cycle_nodes:
                    if dist[v] < min_d:
                        min_d = dist[v]
                if min_d != INF:
                    if 2 * min_d + cycle_len < ans:
                        ans = 2 * min_d + cycle_len
                        
        if ans == INF:
            out.append("-1")
        else:
            out.append(str(ans))
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()