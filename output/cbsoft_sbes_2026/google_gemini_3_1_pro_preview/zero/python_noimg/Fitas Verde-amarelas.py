
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    grid = input_data[2:]
    
    visited = bytearray(N * M)
    total_tapes = 0
    
    for i in range(N):
        row_offset = i * M
        for j in range(M):
            if grid[i][j] == '#' and not visited[row_offset + j]:
                stack = [(i, j)]
                visited[row_offset + j] = 1
                
                h_count = 0
                v_count = 0
                
                while stack:
                    r, c = stack.pop()
                    
                    if c == 0 or grid[r][c-1] == '.':
                        h_count += 1
                    if r == 0 or grid[r-1][c] == '.':
                        v_count += 1
                        
                    if r > 0 and grid[r-1][c] == '#':
                        idx = (r - 1) * M + c
                        if not visited[idx]:
                            visited[idx] = 1
                            stack.append((r-1, c))
                            
                    if r < N - 1 and grid[r+1][c] == '#':
                        idx = (r + 1) * M + c
                        if not visited[idx]:
                            visited[idx] = 1
                            stack.append((r+1, c))
                            
                    if c > 0 and grid[r][c-1] == '#':
                        idx = r * M + c - 1
                        if not visited[idx]:
                            visited[idx] = 1
                            stack.append((r, c-1))
                            
                    if c < M - 1 and grid[r][c+1] == '#':
                        idx = r * M + c + 1
                        if not visited[idx]:
                            visited[idx] = 1
                            stack.append((r, c+1))
                            
                total_tapes += min(h_count, v_count)
                
    print(total_tapes)

if __name__ == '__main__':
    solve()
