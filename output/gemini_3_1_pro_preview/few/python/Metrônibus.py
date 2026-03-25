import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    K1 = int(input_data[1])
    K2 = int(input_data[2])
    P = int(input_data[3])
    
    idx = 4
    
    subway_adj = [[] for _ in range(N + 1)]
    for _ in range(K1):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        subway_adj[u].append(v)
        subway_adj[v].append(u)
        idx += 2
        
    bus_adj = [[] for _ in range(N + 1)]
    for _ in range(K2):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        bus_adj[u].append(v)
        bus_adj[v].append(u)
        idx += 2
        
    A = int(input_data[idx])
    B = int(input_data[idx+1])
    
    if A == B:
        print(0)
        return
        
    subway_comp_of = [-1] * (N + 1)
    subway_comps = []
    
    for i in range(1, N + 1):
        if subway_comp_of[i] == -1 and subway_adj[i]:
            comp_id = len(subway_comps)
            q_comp = [i]
            subway_comp_of[i] = comp_id
            for node in q_comp:
                for neighbor in subway_adj[node]:
                    if subway_comp_of[neighbor] == -1:
                        subway_comp_of[neighbor] = comp_id
                        q_comp.append(neighbor)
            subway_comps.append(q_comp)
            
    bus_comp_of = [-1] * (N + 1)
    bus_comps = []
    
    for i in range(1, N + 1):
        if bus_comp_of[i] == -1 and bus_adj[i]:
            comp_id = len(bus_comps)
            q_comp = [i]
            bus_comp_of[i] = comp_id
            for node in q_comp:
                for neighbor in bus_adj[node]:
                    if bus_comp_of[neighbor] == -1:
                        bus_comp_of[neighbor] = comp_id
                        q_comp.append(neighbor)
            bus_comps.append(q_comp)
            
    dist = [-1] * (N + 1)
    visited_subway_comp = [False] * len(subway_comps)
    visited_bus_comp = [False] * len(bus_comps)
    
    q = deque([A])
    dist[A] = 0
    
    while q:
        u = q.popleft()
        
        s_c = subway_comp_of[u]
        if s_c != -1 and not visited_subway_comp[s_c]:
            visited_subway_comp[s_c] = True
            for v in subway_comps[s_c]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    if v == B:
                        print(dist[v] * P)
                        return
                    q.append(v)
                    
        b_c = bus_comp_of[u]
        if b_c != -1 and not visited_bus_comp[b_c]:
            visited_bus_comp[b_c] = True
            for v in bus_comps[b_c]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    if v == B:
                        print(dist[v] * P)
                        return
                    q.append(v)
                    
    print(-1)

if __name__ == '__main__':
    solve()