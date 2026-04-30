import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    grid = input_data[1:]
    
    unsafe = [[False] * N for _ in range(N)]
    Q = deque()
    
    unsafe_count = 0
    
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'A' and i == 0:
                unsafe[i][j] = True
                Q.append((i, j))
                unsafe_count += 1
            elif grid[i][j] == 'V' and i == N - 1:
                unsafe[i][j] = True
                Q.append((i, j))
                unsafe_count += 1
            elif grid[i][j] == '<' and j == 0:
                unsafe[i][j] = True
                Q.append((i, j))
                unsafe_count += 1
            elif grid[i][j] == '>' and j == N - 1:
                unsafe[i][j] = True
                Q.append((i, j))
                unsafe_count += 1
                
    while Q:
        r, c = Q.popleft()
        
        if r > 0 and not unsafe[r-1][c] and grid[r-1][c] == 'V':
            unsafe[r-1][c] = True
            unsafe_count += 1
            Q.append((r-1, c))
            
        if r < N - 1 and not unsafe[r+1][c] and grid[r+1][c] == 'A':
            unsafe[r+1][c] = True
            unsafe_count += 1
            Q.append((r+1, c))
            
        if c > 0 and not unsafe[r][c-1] and grid[r][c-1] == '>':
            unsafe[r][c-1] = True
            unsafe_count += 1
            Q.append((r, c-1))
            
        if c < N - 1 and not unsafe[r][c+1] and grid[r][c+1] == '<':
            unsafe[r][c+1] = True
            unsafe_count += 1
            Q.append((r, c+1))
            
    print(N * N - unsafe_count)

if __name__ == '__main__':
    solve()