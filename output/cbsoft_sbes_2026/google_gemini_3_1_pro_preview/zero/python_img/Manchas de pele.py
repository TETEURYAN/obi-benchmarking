
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    grid = input_data[2:]
    visited = bytearray(N * M)
    
    spots = 0
    
    for i in range(N):
        for j in range(M):
            idx = i * M + j
            if grid[idx] == '1' and not visited[idx]:
                spots += 1
                stack = [(i, j, idx)]
                visited[idx] = 1
                
                while stack:
                    cx, cy, curr = stack.pop()
                    
                    # Up
                    if cx > 0:
                        n_idx = curr - M
                        if grid[n_idx] == '1' and not visited[n_idx]:
                            visited[n_idx] = 1
                            stack.append((cx - 1, cy, n_idx))
                    # Down
                    if cx < N - 1:
                        n_idx = curr + M
                        if grid[n_idx] == '1' and not visited[n_idx]:
                            visited[n_idx] = 1
                            stack.append((cx + 1, cy, n_idx))
                    # Left
                    if cy > 0:
                        n_idx = curr - 1
                        if grid[n_idx] == '1' and not visited[n_idx]:
                            visited[n_idx] = 1
                            stack.append((cx, cy - 1, n_idx))
                    # Right
                    if cy < M - 1:
                        n_idx = curr + 1
                        if grid[n_idx] == '1' and not visited[n_idx]:
                            visited[n_idx] = 1
                            stack.append((cx, cy + 1, n_idx))
                            
    print(spots)

if __name__ == '__main__':
    solve()
