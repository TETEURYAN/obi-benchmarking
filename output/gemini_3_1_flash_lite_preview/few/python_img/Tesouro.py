import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    M = int(input_data[0])
    grid = input_data[1:M+1]
    A = int(input_data[M+1]) - 1
    B = int(input_data[M+2]) - 1
    
    visited = [[False for _ in range(M)] for _ in range(M)]
    
    curr_r, curr_c = A, B
    time = 0
    
    while 0 <= curr_r < M and 0 <= curr_c < M:
        if grid[curr_r][curr_c] == 'X':
            print(time)
            return
        
        if visited[curr_r][curr_c]:
            print(0)
            return
        
        visited[curr_r][curr_c] = True
        move = grid[curr_r][curr_c]
        
        if move == 'N':
            curr_r -= 1
        elif move == 'S':
            curr_r += 1
        elif move == 'L':
            curr_c += 1
        elif move == 'O':
            curr_c -= 1
            
        time += 1
        
    print(-1)

if __name__ == '__main__':
    solve()