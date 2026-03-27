import sys

def solve():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        m = int(next(iterator))
        n = int(next(iterator))
    except StopIteration:
        return

    grid = []
    for _ in range(m):
        try:
            grid.append(next(iterator))
        except StopIteration:
            break
            
    coast_count = 0
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '#':
                is_coast = False
                
                # Check North
                if i == 0 or grid[i-1][j] == '.':
                    is_coast = True
                # Check South
                elif i == m - 1 or grid[i+1][j] == '.':
                    is_coast = True
                # Check West
                elif j == 0 or grid[i][j-1] == '.':
                    is_coast = True
                # Check East
                elif j == n - 1 or grid[i][j+1] == '.':
                    is_coast = True
                
                if is_coast:
                    coast_count += 1
                    
    print(coast_count)

if __name__ == '__main__':
    solve()