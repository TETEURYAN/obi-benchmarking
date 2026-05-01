import sys

def solve():
    # Fast I/O
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # Use an iterator for clean parsing
    iterator = iter(input_data)
    
    try:
        L = int(next(iterator))
        C = int(next(iterator))
        A = int(next(iterator))
        B = int(next(iterator))
    except StopIteration:
        return

    # Parse grid values
    # We expect L*C integers following the header
    values = list(map(int, iterator))
    
    # Create grid with 0-padding (borders)
    # Dimensions: (L+2) x (C+2)
    # Access: grid[r][c] where 1 <= r <= L, 1 <= c <= C
    grid = [[0] * (C + 2) for _ in range(L + 2)]
    
    # Fill grid
    val_idx = 0
    for r in range(1, L + 1):
        # Slice assignment is faster than nested loops in Python
        grid[r][1 : C + 1] = values[val_idx : val_idx + C]
        val_idx += C
        
    # Current position
    r, c = A, B
    
    # Find the first step
    # The start position has exactly 1 black neighbor.
    # We check 4 directions.
    
    # Directions: Up, Down, Left, Right
    # Up: r-1, c
    if grid[r-1][c] == 1:
        pr, pc = r, c
        r -= 1
    # Down: r+1, c
    elif grid[r+1][c] == 1:
        pr, pc = r, c
        r += 1
    # Left: r, c-1
    elif grid[r][c-1] == 1:
        pr, pc = r, c
        c -= 1
    # Right: r, c+1
    elif grid[r][c+1] == 1:
        pr, pc = r, c
        c += 1
    else:
        # Should not happen based on constraints
        print(f"{A} {B}")
        return

    # Traverse the path
    while True:
        moved = False
        
        # Check Up
        if grid[r-1][c] == 1 and (r-1 != pr or c != pc):
            pr, pc = r, c
            r -= 1
            moved = True
        # Check Down
        elif grid[r+1][c] == 1 and (r+1 != pr or c != pc):
            pr, pc = r, c
            r += 1
            moved = True
        # Check Left
        elif grid[r][c-1] == 1 and (r != pr or c-1 != pc):
            pr, pc = r, c
            c -= 1
            moved = True
        # Check Right
        elif grid[r][c+1] == 1 and (r != pr or c+1 != pc):
            pr, pc = r, c
            c += 1
            moved = True
            
        if not moved:
            # Reached end of path
            print(f"{r} {c}")
            return

if __name__ == "__main__":
    solve()