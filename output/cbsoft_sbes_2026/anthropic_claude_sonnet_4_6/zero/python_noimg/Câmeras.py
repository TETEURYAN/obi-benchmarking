from collections import deque

def solve():
    line = input().split()
    N, M, K = int(line[0]), int(line[1]), int(line[2])
    
    # Grid: columns 1..N (West to East), rows 1..M (North to South)
    # Entry: column 1, row 1 (most North and most West)
    # Exit: column N, row M (most South and most East)
    
    # observed[col][row] = True if observed by any camera
    observed = [[False] * (M + 1) for _ in range(N + 1)]
    
    cameras = []
    for _ in range(K):
        parts = input().split()
        c, l, d = int(parts[0]), int(parts[1]), parts[2]
        cameras.append((c, l, d))
    
    for (c, l, d) in cameras:
        if d == 'N':
            # North: same column, rows from l down to 1 (row 1 is most North)
            for r in range(1, l + 1):
                observed[c][r] = True
        elif d == 'S':
            # South: same column, rows from l up to M
            for r in range(l, M + 1):
                observed[c][r] = True
        elif d == 'L':
            # Leste (East): same row, columns from c up to N
            for col in range(c, N + 1):
                observed[col][l] = True
        elif d == 'O':
            # Oeste (West): same row, columns from c down to 1
            for col in range(1, c + 1):
                observed[col][l] = True
    
    # BFS from (1,1) to (N,M)
    if observed[1][1] or observed[N][M]:
        print('N')
        return
    
    visited = [[False] * (M + 1) for _ in range(N + 1)]
    visited[1][1] = True
    queue = deque()
    queue.append((1, 1))
    
    # Directions: North (row-1), South (row+1), East (col+1), West (col-1)
    dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    
    found = False
    while queue:
        col, row = queue.popleft()
        if col == N and row == M:
            found = True
            break
        for dc, dr in dirs:
            nc, nr = col + dc, row + dr
            if 1 <= nc <= N and 1 <= nr <= M and not visited[nc][nr] and not observed[nc][nr]:
                visited[nc][nr] = True
                queue.append((nc, nr))
    
    print('S' if found else 'N')

solve()