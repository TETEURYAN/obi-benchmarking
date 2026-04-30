
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    grid = input_data[1:]
    
    # state: 0 = unvisited, 1 = visiting, 2 = safe, 3 = unsafe
    state = [[0] * N for _ in range(N)]
    safe_count = 0
    
    for i in range(N):
        for j in range(N):
            if state[i][j] == 0:
                path = []
                curr_i, curr_j = i, j
                status = -1
                
                while True:
                    if curr_i < 0 or curr_i >= N or curr_j < 0 or curr_j >= N:
                        status = 3
                        break
                    
                    st = state[curr_i][curr_j]
                    if st != 0:
                        if st == 1:
                            status = 2
                        else:
                            status = st
                        break
                    
                    state[curr_i][curr_j] = 1
                    path.append((curr_i, curr_j))
                    
                    char = grid[curr_i][curr_j]
                    if char == 'V':
                        curr_i += 1
                    elif char == '<':
                        curr_j -= 1
                    elif char == '>':
                        curr_j += 1
                    elif char == 'A':
                        curr_i -= 1
                
                for pi, pj in path:
                    state[pi][pj] = status
                    if status == 2:
                        safe_count += 1

    print(safe_count)

if __name__ == '__main__':
    solve()
