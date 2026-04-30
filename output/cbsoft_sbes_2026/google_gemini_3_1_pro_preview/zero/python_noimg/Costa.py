import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    M = int(input_data[0])
    N = int(input_data[1])
    grid = input_data[2:]
    
    coast_count = 0
    
    coast_count += grid[0].count('#')
    if M > 1:
        coast_count += grid[M-1].count('#')
        
    for i in range(1, M - 1):
        row = grid[i]
        prev_row = grid[i-1]
        next_row = grid[i+1]
        
        if row[0] == '#':
            coast_count += 1
        if N > 1 and row[N-1] == '#':
            coast_count += 1
            
        for j in range(1, N - 1):
            if row[j] == '#':
                if prev_row[j] == '.' or next_row[j] == '.' or row[j-1] == '.' or row[j+1] == '.':
                    coast_count += 1
                        
    print(coast_count)

if __name__ == '__main__':
    solve()