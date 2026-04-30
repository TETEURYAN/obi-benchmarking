
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    M = int(input_data[0])
    grid = input_data[1:M+1]
    A = int(input_data[M+1])
    B = int(input_data[M+2])
    
    r = A - 1
    c = B - 1
    
    visited = bytearray(M * M)
    steps = 0
    
    while True:
        if r < 0 or r >= M or c < 0 or c >= M:
            print("-1")
            return
        
        cell = grid[r][c]
        
        if cell == 'X':
            print(steps)
            return
            
        idx = r * M + c
        if visited[idx]:
            print("0")
            return
            
        visited[idx] = 1
        steps += 1
        
        if cell == 'N':
            r -= 1
        elif cell == 'S':
            r += 1
        elif cell == 'L':
            c += 1
        elif cell == 'O':
            c -= 1

if __name__ == '__main__':
    solve()
