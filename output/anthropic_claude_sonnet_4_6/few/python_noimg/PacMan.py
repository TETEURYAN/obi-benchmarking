import sys

def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    grid = []
    for i in range(1, n + 1):
        grid.append(data[i])
    
    # Simulate the path and track cumulative food
    # At each cell, we track running food count
    # If we hit a ghost, food resets to 0
    # We want the maximum food at any point (including end)
    
    max_food = 0
    current_food = 0
    
    for row in range(n):
        if row % 2 == 0:
            # left to right
            cols = range(n)
        else:
            # right to left
            cols = range(n - 1, -1, -1)
        
        for col in cols:
            # Skip starting position (0,0) which is guaranteed empty
            cell = grid[row][col] if col < len(grid[row]) else '.'
            
            if cell == 'A':
                current_food = 0
            elif cell == 'o':
                current_food += 1
            
            if current_food > max_food:
                max_food = current_food
    
    print(max_food)

solve()