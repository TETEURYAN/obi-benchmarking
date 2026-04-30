import sys

def solve():
    grid = sys.stdin.read().split()
    if not grid:
        return
    
    N = int(grid[0])
    M = int(grid[1])
    
    count = 0
    total = N * M
    limit = total + 2
    
    for i in range(2, limit):
        if grid[i] == '1':
            count += 1
            stack = [i]
            grid[i] = '0'
            while stack:
                curr = stack.pop()
                
                up = curr - M
                if up >= 2 and grid[up] == '1':
                    grid[up] = '0'
                    stack.append(up)
                
                down = curr + M
                if down < limit and grid[down] == '1':
                    grid[down] = '0'
                    stack.append(down)
                
                if (curr - 2) % M != 0:
                    left = curr - 1
                    if grid[left] == '1':
                        grid[left] = '0'
                        stack.append(left)
                
                if (curr - 1) % M != 0:
                    right = curr + 1
                    if grid[right] == '1':
                        grid[right] = '0'
                        stack.append(right)

    print(count)

if __name__ == '__main__':
    solve()