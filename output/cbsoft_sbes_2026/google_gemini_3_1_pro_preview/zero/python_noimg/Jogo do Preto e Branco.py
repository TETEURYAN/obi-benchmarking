
import sys

# Aumentar o limite de recursão por precaução, embora não seja estritamente necessário para L, C <= 6
sys.setrecursionlimit(2000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    L = int(input_data[0])
    C = int(input_data[1])
    P = int(input_data[2])
    
    B = set()
    idx = 3
    for _ in range(P):
        r = int(input_data[idx]) - 1
        c = int(input_data[idx+1]) - 1
        B.add((r, c))
        idx += 2
        
    S = set()
    for r in range(L):
        for c in range(C):
            if (r, c) in B:
                continue
            is_adj_to_B = False
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if (nr, nc) in B:
                    is_adj_to_B = True
                    break
            if is_adj_to_B:
                S.add((r, c))
                
    S_even = [u for u in S if (u[0] + u[1]) % 2 == 0]
    S_odd = {u for u in S if (u[0] + u[1]) % 2 != 0}
    
    graph = {u: [] for u in S_even}
    for u in S_even:
        r, c = u
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if (nr, nc) in S_odd:
                graph[u].append((nr, nc))
                
    match = {}
    
    def dfs(u, visited):
        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                if v not in match or dfs(match[v], visited):
                    match[v] = u
                    return True
        return False

    matching_size = 0
    for u in S_even:
        visited = set()
        if dfs(u, visited):
            matching_size += 1
            
    print(len(S) - matching_size)

if __name__ == '__main__':
    solve()
