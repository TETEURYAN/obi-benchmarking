from collections import deque

def solve():
    line = input().split()
    N, M = int(line[0]), int(line[1])
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
    visited = set()
    queue = deque()
    queue.append((SC, SL))
    visited.add((SC, SL))
    
    # Can jump 1, 2, or 3 meters in parallel directions (horizontal or vertical)
    directions = []
    for d in [1, 2, 3]:
        directions.append((d, 0))
        directions.append((-d, 0))
        directions.append((0, d))
        directions.append((0, -d))
    
    found = False
    while queue:
        c, l = queue.popleft()
        if c == RC and l == RL:
            found = True
            break
        for dc, dl in directions:
            nc, nl = c + dc, l + dl
            if (nc, nl) in stones and (nc, nl) not in visited:
                visited.add((nc, nl))
                queue.append((nc, nl))
    
    print('S' if found else 'N')

solve()