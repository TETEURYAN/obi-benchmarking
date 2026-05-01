import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    M = int(input_data[0])
    N = int(input_data[1])
    grid = input_data[2:]
    
    coast_count = 0
    
    for i in range(M):
        row = grid[i]
        for j in range(N):
            if row[j] == '#':
                if i == 0 or i == M - 1 or j == 0 or j == N - 1 \
                   or grid[i-1][j] == '.' or grid[i+1][j] == '.' \
                   or row[j-1] == '.' or row[j+1] == '.':
                    coast_count += 1
                    
    print(coast_count)

if __name__ == '__main__':
    solve()