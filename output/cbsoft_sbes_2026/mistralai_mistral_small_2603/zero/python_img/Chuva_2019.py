
import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    N, M = map(int, data[0].split())
    grid = [list(line.strip()) for line in data[1:1+N]]

    # Find the initial 'o' in the first row
    start_col = -1
    for j in range(M):
        if grid[0][j] == 'o':
            start_col = j
            break

    # Directions: down, left, right
    # We'll process the grid in a BFS-like manner, but respecting the rules
    # Since the rules are complex, we'll simulate the water flow step by step

    # We'll use a queue to process cells that need to be processed
    from collections import deque
    q = deque()

    # Initialize the queue with the starting 'o' and mark it as processed
    q.append((0, start_col))
    grid[0][start_col] = 'o'

    while q:
        i, j = q.popleft()

        # Check the cell below (i+1, j)
        if i + 1 < N and grid[i+1][j] == '.':
            grid[i+1][j] = 'o'
            q.append((i+1, j))

        # Check left and right for horizontal spreading
        # Left side
        if j > 0:
            # Check if we can spread left
            if grid[i][j-1] == '.' and (i == 0 or (i % 2 == 1 and grid[i-1][j-1] == '#')):
                grid[i][j-1] = 'o'
                q.append((i, j-1))
            # Check if we can spread left and then down
            if i + 1 < N and grid[i+1][j-1] == '#' and grid[i][j-1] == 'o':
                # Then the cell below the left can be filled if it's '.'
                if grid[i+1][j-1] == '#' and i + 2 < N and grid[i+2][j-1] == '.':
                    grid[i+2][j-1] = 'o'
                    q.append((i+2, j-1))

        # Right side
        if j < M - 1:
            # Check if we can spread right
            if grid[i][j+1] == '.' and (i == 0 or (i % 2 == 1 and grid[i-1][j+1] == '#')):
                grid[i][j+1] = 'o'
                q.append((i, j+1))
            # Check if we can spread right and then down
            if i + 1 < N and grid[i+1][j+1] == '#' and grid[i][j+1] == 'o':
                # Then the cell below the right can be filled if it's '.'
                if grid[i+1][j+1] == '#' and i + 2 < N and grid[i+2][j+1] == '.':
                    grid[i+2][j+1] = 'o'
                    q.append((i+2, j+1))

    # After processing, we need to handle the horizontal spreading properly
    # The above approach may not cover all cases, so we'll do a more thorough simulation

    # Alternative approach: simulate the water flow in layers
    # We'll process each row and propagate the water according to the rules

    # Reset the grid to original and re-process
    # Since the above may not work, let's try a different approach

    # Re-read the input
    data = sys.stdin.read().splitlines()
    if not data:
        return
    N, M = map(int, data[0].split())
    grid = [list(line.strip()) for line in data[1:1+N]]

    # Find the initial 'o'
    start_col = -1
    for j in range(M):
        if grid[0][j] == 'o':
            start_col = j
            break

    # We'll process the grid in a BFS manner, but respecting the rules
    # The rules are:
    # 1. If the cell above is 'o', then this cell becomes 'o'
    # 2. If the left cell is 'o' and the cell below-left is '#', then this cell becomes 'o'
    # 3. If the right cell is 'o' and the cell below-right is '#', then this cell becomes 'o'

    # We'll use a queue to process cells
    q = deque()
    q.append((0, start_col))
    grid[0][start_col] = 'o'

    while q:
        i, j = q.popleft()

        # Rule 1: cell above is 'o'
        if i > 0 and grid[i-1][j] == 'o' and grid[i][j] == '.':
            grid[i][j] = 'o'
            q.append((i, j))

        # Rule 2: left cell is 'o' and below-left is '#'
        if j > 0 and grid[i][j-1] == 'o' and i + 1 < N and grid[i+1][j-1] == '#' and grid[i][j] == '.':
            grid[i][j] = 'o'
            q.append((i, j))

        # Rule 3: right cell is 'o' and below-right is '#'
        if j < M - 1 and grid[i][j+1] == 'o' and i + 1 < N and grid[i+1][j+1] == '#' and grid[i][j] == '.':
            grid[i][j] = 'o'
            q.append((i, j))

    # After processing, we need to handle the horizontal spreading
    # The above may not cover all cases, so we'll do a more thorough simulation

    # Let's try a different approach: simulate the water flow in layers
    # We'll process each row and propagate the water according to the rules

    # Re-read the input again
    data = sys.stdin.read().splitlines()
    if not data:
        return
    N, M = map(int, data[0].split())
    grid = [list(line.strip()) for line in data[1:1+N]]

    # Find the initial 'o'
    start_col = -1
    for j in range(M):
        if grid[0][j] == 'o':
            start_col = j
            break

    # We'll process the grid in a BFS manner, but respecting the rules
    # The rules are:
    # 1. If the cell above is 'o', then this cell becomes 'o'
    # 2. If the left cell is 'o' and the cell below-left is '#', then this cell becomes 'o'
    # 3. If the right cell is 'o' and the cell below-right is '#', then this cell becomes 'o'

    # We'll use a queue to process cells
    q = deque()
    q.append((0, start_col))
    grid[0][start_col] = 'o'

    changed = True
    while changed:
        changed = False
        new_grid = [row[:] for row in grid]
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 'o':
                    continue
                # Rule 1: cell above is 'o'
                if i > 0 and grid[i-1][j] == 'o':
                    new_grid[i][j] = 'o'
                    changed = True
                # Rule 2: left cell is 'o' and below-left is '#'
                elif j > 0 and grid[i][j-1] == 'o' and i + 1 < N and grid[i+1][j-1] == '#':
                    new_grid[i][j] = 'o'
                    changed = True
                # Rule 3: right cell is 'o' and below-right is '#'
                elif j < M - 1 and grid[i][j+1] == 'o' and i + 1 < N and grid[i+1][j+1] == '#':
                    new_grid[i][j] = 'o'
                    changed = True
        grid = new_grid

    # Print the result
    for row in grid:
        print(''.join(row))

if __name__ == '__main__':
    main()
