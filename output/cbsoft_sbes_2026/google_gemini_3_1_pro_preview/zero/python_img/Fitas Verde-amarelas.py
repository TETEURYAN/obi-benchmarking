import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    grid = input_data[2:]
    
    comp_id = [-1] * (N * M)
    current_id = 0
    
    for i in range(N):
        row_offset = i * M
        for j in range(M):
            if grid[i][j] == '#' and comp_id[row_offset + j] == -1:
                queue = deque([(i, j)])
                comp_id[row_offset + j] = current_id
                
                while queue:
                    r, c = queue.popleft()
                    idx = r * M + c
                    
                    if r > 0 and grid[r-1][c] == '#' and comp_id[idx - M] == -1:
                        comp_id[idx - M] = current_id
                        queue.append((r-1, c))
                    if r < N - 1 and grid[r+1][c] == '#' and comp_id[idx + M] == -1:
                        comp_id[idx + M] = current_id
                        queue.append((r+1, c))
                    if c > 0 and grid[r][c-1] == '#' and comp_id[idx - 1] == -1:
                        comp_id[idx - 1] = current_id
                        queue.append((r, c-1))
                    if c < M - 1 and grid[r][c+1] == '#' and comp_id[idx + 1] == -1:
                        comp_id[idx + 1] = current_id
                        queue.append((r, c+1))
                        
                current_id += 1
                
    h_counts = [0] * current_id
    v_counts = [0] * current_id
    
    for i in range(N):
        in_segment = False
        row_offset = i * M
        row_str = grid[i]
        for j in range(M):
            if row_str[j] == '#':
                if not in_segment:
                    in_segment = True
                    h_counts[comp_id[row_offset + j]] += 1
            else:
                in_segment = False
                
    for j in range(M):
        in_segment = False
        for i in range(N):
            if grid[i][j] == '#':
                if not in_segment:
                    in_segment = True
                    v_counts[comp_id[i * M + j]] += 1
            else:
                in_segment = False
                
    total_cost = sum(min(h_counts[k], v_counts[k]) for k in range(current_id))
    print(total_cost)

if __name__ == '__main__':
    solve()