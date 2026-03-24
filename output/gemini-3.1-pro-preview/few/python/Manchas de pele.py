import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    grid = input_data[2:]
    
    count = 0
    for i in range(N * M):
        if grid[i] == '1':
            count += 1
            grid[i] = '0'
            stack = [i]
            while stack:
                curr = stack.pop()
                r = curr // M
                c = curr % M
                
                if r > 0:
                    nxt = curr - M
                    if grid[nxt] == '1':
                        grid[nxt] = '0'
                        stack.append(nxt)
                if r < N - 1:
                    nxt = curr + M
                    if grid[nxt] == '1':
                        grid[nxt] = '0'
                        stack.append(nxt)
                if c > 0:
                    nxt = curr - 1
                    if grid[nxt] == '1':
                        grid[nxt] = '0'
                        stack.append(nxt)
                if c < M - 1:
                    nxt = curr + 1
                    if grid[nxt] == '1':
                        grid[nxt] = '0'
                        stack.append(nxt)
                        
    print(count)

if __name__ == '__main__':
    solve()