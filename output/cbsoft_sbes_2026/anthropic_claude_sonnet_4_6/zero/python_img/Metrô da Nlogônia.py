
import sys
from collections import deque

def bfs(graph, start, n):
    dist = [-1] * (n + 1)
    dist[start] = 0
    q = deque([start])
    while q:
        u = q.popleft()
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist

def find_diameter_and_center(graph, n):
    # BFS from node 1 to find farthest node
    d1 = bfs(graph, 1, n)
    far1 = max(range(1, n+1), key=lambda x: d1[x])
    
    # BFS from far1
    d2 = bfs(graph, far1, n)
    far2 = max(range(1, n+1), key=lambda x: d2[x])
    
    diameter = d2[far2]
    
    # BFS from far2
    d3 = bfs(graph, far2, n)
    
    # For each node, its eccentricity within the tree is max(d2[node], d3[node])
    # The center nodes minimize this eccentricity
    # The "radius" of the tree is ceil(diameter/2)
    # Center nodes are those where max(d2[node], d3[node]) == ceil(diameter/2)
    
    radius = (diameter + 1) // 2
    
    # Find all nodes that are on the diameter path and have eccentricity = radius
    # Actually, we want nodes that minimize max(d2[node], d3[node])
    min_ecc = min(max(d2[i], d3[i]) for i in range(1, n+1))
    
    center_nodes = [i for i in range(1, n+1) if max(d2[i], d3[i]) == min_ecc]
    
    return diameter, min_ecc, center_nodes, d2, d3

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(input_data[idx]); idx+=1
    M = int(input_data[idx]); idx+=1
    
    graphC = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a = int(input_data[idx]); idx+=1
        b = int(input_data[idx]); idx+=1
        graphC[a].append(b)
        graphC[b].append(a)
    
    graphS = [[] for _ in range(M+1)]
    for _ in range(M-1):
        x = int(input_data[idx]); idx+=1
        y = int(input_data[idx]); idx+=1
        graphS[x].append(y)
        graphS[y].append(x)
    
    # Find diameter and center for Circle system
    diamC, radC, centersC, d2C, d3C = find_diameter_and_center(graphC, N)
    
    # Find diameter and center for Square system
    diamS, radS, centersS, d2S, d3S = find_diameter_and_center(graphS, M)
    
    # When we connect node u from C and node v from S,
    # the new diameter is max(diamC, diamS, radC_u + 1 + radS_v)
    # where radC_u = max(d2C[u], d3C[u]) and radS_v = max(d2S[v], d3S[v])
    # We want to minimize this.
    # The minimum of radC_u + radS_v is radC + radS (using center nodes)
    # So the answer is max(diamC, diamS, radC + 1 + radS)
    
    # Best node from C: minimize max(d2C[u], d3C[u]) -> use centersC
    # Best node from S: minimize max(d2S[v], d3S[v]) -> use centersS
    
    best_c = centersC[0]
    best_s = centersS[0]
    
    print(best_c, best_s)

solve()
