import sys
from collections import deque

def bfs_farthest(start, adj, n):
    dist = [-1] * (n + 1)
    dist[start] = 0
    q = deque([start])
    farthest = start
    max_dist = 0
    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                if dist[v] > max_dist:
                    max_dist = dist[v]
                    farthest = v
                q.append(v)
    return farthest, max_dist, dist

def get_diameter_and_eccentricities(adj, n):
    # Find diameter endpoints
    u, _, _ = bfs_farthest(1, adj, n)
    v, diam, dist_u = bfs_farthest(u, adj, n)
    _, _, dist_v = bfs_farthest(v, adj, n)
    
    # Eccentricity of node i = max(dist_u[i], dist_v[i])
    # This gives the exact eccentricity for trees
    ecc = [0] * (n + 1)
    for i in range(1, n + 1):
        ecc[i] = max(dist_u[i], dist_v[i])
    
    return diam, ecc

def solve():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
    
    adjC = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a = int(data[idx]); idx += 1
        b = int(data[idx]); idx += 1
        adjC[a].append(b)
        adjC[b].append(a)
    
    adjS = [[] for _ in range(M + 1)]
    for _ in range(M - 1):
        x = int(data[idx]); idx += 1
        y = int(data[idx]); idx += 1
        adjS[x].append(y)
        adjS[y].append(x)
    
    diamC, eccC = get_diameter_and_eccentricities(adjC, N)
    diamS, eccS = get_diameter_and_eccentricities(adjS, M)
    
    # When we connect node c from C and node s from S,
    # the diameter of integrated system is:
    # max(diamC, diamS, eccC[c] + 1 + eccS[s])
    # We want to minimize this over all pairs (c, s)
    
    # The minimum possible value of eccC[c] + 1 + eccS[s] is
    # min(eccC) + 1 + min(eccS)
    # But we also have floor constraints from diamC and diamS
    
    # So the answer diameter = max(diamC, diamS, min_eccC + 1 + min_eccS)
    # where min_eccC = ceil(diamC/2), min_eccS = ceil(diamS/2)
    
    # We need to find c with minimum eccentricity and s with minimum eccentricity
    # The minimum eccentricity in a tree = ceil(diameter/2)
    
    min_eccC = (diamC + 1) // 2
    min_eccS = (diamS + 1) // 2
    
    # Find best c: node in C with ecc[c] == min_eccC
    best_c = -1
    for i in range(1, N + 1):
        if eccC[i] == min_eccC:
            best_c = i
            break
    
    # Find best s: node in S with ecc[s] == min_eccS
    best_s = -1
    for i in range(1, M + 1):
        if eccS[i] == min_eccS:
            best_s = i
            break
    
    print(best_c, best_s)

solve()