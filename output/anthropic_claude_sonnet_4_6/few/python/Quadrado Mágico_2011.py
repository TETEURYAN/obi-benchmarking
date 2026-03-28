import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    grid = []
    for i in range(n):
        row = [int(data[idx+j]) for j in range(n)]
        idx += n
        grid.append(row)
    
    # Check contains 1..N^2
    expected = set(range(1, n*n+1))
    actual = set()
    for row in grid:
        for v in row:
            actual.add(v)
    if actual != expected:
        print(0)
        return
    
    # Magic constant: sum of first row
    magic = sum(grid[0])
    
    # Check all rows
    for i in range(1, n):
        if sum(grid[i]) != magic:
            print(0)
            return
    
    # Check all columns
    for j in range(n):
        s = 0
        for i in range(n):
            s += grid[i][j]
        if s != magic:
            print(0)
            return
    
    # Check main diagonal
    s = sum(grid[i][i] for i in range(n))
    if s != magic:
        print(0)
        return
    
    # Check anti-diagonal
    s = sum(grid[i][n-1-i] for i in range(n))
    if s != magic:
        print(0)
        return
    
    print(magic)

solve()