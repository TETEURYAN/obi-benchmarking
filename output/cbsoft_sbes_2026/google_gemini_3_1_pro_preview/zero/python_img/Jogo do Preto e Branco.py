
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
        r = int(input_data[idx])
        c = int(input_data[idx+1])
        B.add((r, c))
        idx += 2
        
    S = set()
    for r in range(1, L + 1):
        for c in range(1, C + 1):
            if (r, c) in B:
                continue
            
            is_candidate = False
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if (nr, nc) in B:
                    is_candidate = True
                    break
            
            if is_candidate:
                S.add((r, c))
                
    Odd = []
    Even = set()
    for r, c in S:
        if (r + c) % 2 != 0:
            Odd.append((r, c))
        else:
            Even.add((r, c))
            
    adj = {u: [] for u in Odd}
    for r, c in Odd:
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if (nr, nc) in Even:
                adj[(r, c)].append((nr, nc))
                
    match = {}
    
    def dfs(u, visited):
        for v in adj[u]:
            if v not in visited:
                visited.add(v)
                if v not in match or dfs(match[v], visited):
                    match[v] = u
                    return True
        return False

    matching_size = 0
    for u in Odd:
        visited = set()
        if dfs(u, visited):
            matching_size += 1
            
    print(len(S) - matching_size)

if __name__ == '__main__':
    solve()
