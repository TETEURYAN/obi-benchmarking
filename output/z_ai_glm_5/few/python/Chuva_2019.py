import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        N = int(next(iterator))
        M = int(next(iterator))
    except StopIteration:
        return

    grid = []
    for _ in range(N):
        try:
            grid.append(list(next(iterator)))
        except StopIteration:
            grid.append(['.'] * M)

    # Initialize wet array for the first row
    wet = [False] * M
    for j in range(M):
        if grid[0][j] == 'o':
            wet[j] = True
            grid[0][j] = '.' # Treat as empty for logic, wet array tracks state

    for i in range(N):
        next_wet = [False] * M
        
        # Process current row to determine wet spots and next row's wet spots
        j = 0
        while j < M:
            if wet[j]:
                # Check if we are at the bottom
                if i + 1 == N:
                    pass # No flow downwards
                else:
                    below = grid[i+1][j]
                    if below == '.':
                        # Drip down
                        next_wet[j] = True
                    elif below == '#':
                        # Hit a shelf, spread horizontally
                        # Find extent of the shelf
                        l = j
                        while l >= 0 and grid[i+1][l] == '#':
                            l -= 1
                        l += 1
                        
                        r = j
                        while r < M and grid[i+1][r] == '#':
                            r += 1
                        r -= 1
                        
                        # Spread on current row
                        # Water flows to l-1 and r+1
                        # The cells l to r are above the shelf
                        # The water covers l to r, and flows to l-1 and r+1
                        
                        # Mark current row wet spots
                        for k in range(l, r + 1):
                            wet[k] = True
                        
                        # Drip at ends
                        if l - 1 >= 0:
                            wet[l-1] = True # Flow on current row
                            next_wet[l-1] = True # Drip to next
                        if r + 1 < M:
                            wet[r+1] = True # Flow on current row
                            next_wet[r+1] = True # Drip to next
                        
                        # Skip processed part of the shelf
                        j = r
            
            j += 1
            
        # Print current row
        row_str = []
        for k in range(M):
            if grid[i][k] == '#':
                row_str.append('#')
            elif wet[k]:
                row_str.append('o')
            else:
                row_str.append('.')
        print("".join(row_str))
        
        wet = next_wet

if __name__ == '__main__':
    solve()