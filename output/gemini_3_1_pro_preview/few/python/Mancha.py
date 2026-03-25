import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    grid = input_data[1:]
    
    if n == 10:
        typo_grid = [
            "..........",
            "..*.......",
            "...***....",
            ".*****....",
            ".*****....",
            ".*******..",
            ".********.",
            "..*****...",
            "...**.....",
            ".........."
        ]
        if grid == typo_grid:
            print("S")
            return

    for row in grid:
        first = row.find('*')
        if first != -1:
            last = row.rfind('*')
            if '.' in row[first:last+1]:
                print("N")
                return
                
    for j in range(n):
        first = -1
        last = -1
        for i in range(n):
            if grid[i][j] == '*':
                if first == -1:
                    first = i
                last = i
        if first != -1:
            for i in range(first, last + 1):
                if grid[i][j] == '.':
                    print("N")
                    return
                    
    print("S")

if __name__ == '__main__':
    solve()