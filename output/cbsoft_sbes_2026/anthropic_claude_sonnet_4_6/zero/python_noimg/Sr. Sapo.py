from collections import deque

def solve():
    line1 = input().split()
    N, M = int(line1[0]), int(line1[1])
    
    P = int(input())
    stones = set()
    
    for _ in range(P):
        parts = input().split()
        c, l = int(parts[0]), int(parts[1])
        stones.add((c, l))
    
    start_parts = input().split()
    SC, SL = int(start_parts[0]), int(start_parts[1])
    
    end_parts = input().split()
    RC, RL = int(end_parts[0]), int(end_parts[1])
    
    # BFS
    queue = deque()
    queue.append((SC, SL))
    visited = set()
    visited.add((SC, SL))
    
    found = False
    
    while queue:
        c, l = queue.popleft()
        
        if c == RC and l == RL:
            found = True
            break
        
        # Can jump 1, 2, or 3 in parallel directions (horizontal or vertical)
        for dc in [-3, -2, -1, 1, 2, 3]:
            nc = c + dc
            nl = l
            if (nc, nl) in stones and (nc, nl) not in visited:
                visited.add((nc, nl))
                queue.append((nc, nl))
        
        for dl in [-3, -2, -1, 1, 2, 3]:
            nc = c
            nl = l + dl
            if (nc, nl) in stones and (nc, nl) not in visited:
                visited.add((nc, nl))
                queue.append((nc, nl))
    
    print('S' if found else 'N')

solve()