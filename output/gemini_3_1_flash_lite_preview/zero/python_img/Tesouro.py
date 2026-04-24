import sys

def solve():
    try:
        line1 = sys.stdin.readline()
        if not line1:
            return
        m = int(line1.strip())
    except ValueError:
        return

    grid = [sys.stdin.readline().strip() for _ in range(m)]
    
    try:
        start_coords = sys.stdin.readline().split()
        if not start_coords:
            return
        r, c = map(int, start_coords)
    except ValueError:
        return

    # Ajuste para índice 0
    curr_r, curr_c = r - 1, c - 1
    
    visited = [[False for _ in range(m)] for _ in range(m)]
    time = 0
    
    while 0 <= curr_r < m and 0 <= curr_c < m:
        char = grid[curr_r][curr_c]
        
        if char == 'X':
            print(time)
            return
        
        if visited[curr_r][curr_c]:
            print(0)
            return
        
        visited[curr_r][curr_c] = True
        
        if char == 'N':
            curr_r -= 1
        elif char == 'S':
            curr_r += 1
        elif char == 'L':
            curr_c += 1
        elif char == 'O':
            curr_c -= 1
            
        time += 1
        
    print(-1)

if __name__ == '__main__':
    solve()