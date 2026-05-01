
import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    K = int(input_data[2])
    
    observed = [[False] * M for _ in range(N)]
    
    idx = 3
    for _ in range(K):
        c = int(input_data[idx]) - 1
        r = int(input_data[idx+1]) - 1
        d = input_data[idx+2]
        idx += 3
        
        if d == 'N':
            for y in range(r, -1, -1):
                observed[c][y] = True
        elif d == 'S':
            for y in range(r, M):
                observed[c][y] = True
        elif d == 'L':
            for x in range(c, N):
                observed[x][r] = True
        elif d == 'O':
            for x in range(c, -1, -1):
                observed[x][r] = True
                
    if observed[0][0] or observed[N-1][M-1]:
        print('N')
        return
        
    queue = deque([(0, 0)])
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    
    while queue:
        x, y = queue.popleft()
        
        if x == N - 1 and y == M - 1:
            print('S')
            return
            
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if not observed[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    
    print('N')

if __name__ == '__main__':
    solve()
