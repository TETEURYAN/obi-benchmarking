import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx+=1
    M = int(data[idx]); idx+=1
    K = int(data[idx]); idx+=1
    
    # Grid: columns 1..N (West to East), rows 1..M (North to South)
    # observed[col][row] = True if observed by any camera
    observed = [[False]*(M+1) for _ in range(N+1)]
    
    for _ in range(K):
        c = int(data[idx]); idx+=1
        l = int(data[idx]); idx+=1
        d = data[idx]; idx+=1
        
        if d == 'N':
            # North: decreasing row (row 1 is northmost)
            for row in range(l, 0, -1):
                observed[c][row] = True
        elif d == 'S':
            # South: increasing row
            for row in range(l, M+1):
                observed[c][row] = True
        elif d == 'O':
            # West: decreasing column
            for col in range(c, 0, -1):
                observed[col][l] = True
        elif d == 'L':
            # East: increasing column
            for col in range(c, N+1):
                observed[col][l] = True
    
    # Entry: northmost and westmost = column 1, row 1
    # Exit: southmost and eastmost = column N, row M
    start = (1, 1)
    end = (N, M)
    
    if observed[1][1] or observed[N][M]:
        print('N')
        return
    
    visited = [[False]*(M+1) for _ in range(N+1)]
    visited[1][1] = True
    queue = deque()
    queue.append(start)
    
    # Directions: N(row-1), S(row+1), O(col-1), L(col+1)
    dirs = [(0,-1),(0,1),(-1,0),(1,0)]
    
    found = False
    while queue:
        col, row = queue.popleft()
        if col == N and row == M:
            found = True
            break
        for dc, dr in dirs:
            nc, nr = col+dc, row+dr
            if 1 <= nc <= N and 1 <= nr <= M and not visited[nc][nr] and not observed[nc][nr]:
                visited[nc][nr] = True
                queue.append((nc, nr))
    
    print('S' if found else 'N')

solve()