from collections import deque

def solve():
    line = input().split()
    N, M, K = int(line[0]), int(line[1]), int(line[2])
    
    # Grid: columns 1..N (West to East), lines 1..M (North to South)
    # Entry: column 1, line 1 (most North and most West)
    # Exit: column N, line M (most South and most East)
    
    # observed[col][line] = True if observed by any camera
    observed = [[False] * (M + 1) for _ in range(N + 1)]
    
    for _ in range(K):
        parts = input().split()
        c, l, d = int(parts[0]), int(parts[1]), parts[2]
        
        if d == 'N':
            # North: decreasing line numbers (line 1 is most North)
            for li in range(l, 0, -1):
                observed[c][li] = True
        elif d == 'S':
            # South: increasing line numbers
            for li in range(l, M + 1):
                observed[c][li] = True
        elif d == 'L':
            # East (Leste): increasing column numbers
            for ci in range(c, N + 1):
                observed[ci][l] = True
        elif d == 'O':
            # West (Oeste): decreasing column numbers
            for ci in range(c, 0, -1):
                observed[ci][l] = True
    
    # BFS from (1,1) to (N,M)
    # Check if start and end are not observed
    if observed[1][1] or observed[N][M]:
        print('N')
        return
    
    visited = [[False] * (M + 1) for _ in range(N + 1)]
    visited[1][1] = True
    queue = deque()
    queue.append((1, 1))
    
    # Directions: North (line-1), South (line+1), East/Leste (col+1), West/Oeste (col-1)
    dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    
    found = False
    while queue:
        c, l = queue.popleft()
        if c == N and l == M:
            found = True
            break
        for dc, dl in dirs:
            nc, nl = c + dc, l + dl
            if 1 <= nc <= N and 1 <= nl <= M and not visited[nc][nl] and not observed[nc][nl]:
                visited[nc][nl] = True
                queue.append((nc, nl))
    
    print('S' if found else 'N')

solve()