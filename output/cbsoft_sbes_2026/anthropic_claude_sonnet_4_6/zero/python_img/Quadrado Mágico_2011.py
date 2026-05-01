import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    grid = []
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)
    
    # Check if numbers 1 to n^2 are used exactly once
    flat = []
    for row in grid:
        flat.extend(row)
    
    if sorted(flat) != list(range(1, n*n+1)):
        print(0)
        return
    
    # Calculate magic sum from first row
    magic_sum = sum(grid[0])
    
    # Check all rows
    for i in range(1, n):
        if sum(grid[i]) != magic_sum:
            print(0)
            return
    
    # Check all columns
    for j in range(n):
        col_sum = sum(grid[i][j] for i in range(n))
        if col_sum != magic_sum:
            print(0)
            return
    
    # Check main diagonal
    diag1 = sum(grid[i][i] for i in range(n))
    if diag1 != magic_sum:
        print(0)
        return
    
    # Check anti-diagonal
    diag2 = sum(grid[i][n-1-i] for i in range(n))
    if diag2 != magic_sum:
        print(0)
        return
    
    print(magic_sum)

solve()