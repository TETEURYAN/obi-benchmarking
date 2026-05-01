
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    grid = input_data[1:N+1]
    
    for row in grid:
        if '.' in row.strip('.'):
            print("N")
            return
            
    for col in zip(*grid):
        if '.' in "".join(col).strip('.'):
            print("N")
            return
            
    print("S")

if __name__ == '__main__':
    solve()
