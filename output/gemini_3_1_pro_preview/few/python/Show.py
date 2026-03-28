import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    A = int(input_data[0])
    N = int(input_data[1])
    M = int(input_data[2])
    
    grid = []
    idx = 3
    for _ in range(N):
        row = []
        for _ in range(M):
            row.append(int(input_data[idx]))
            idx += 1
        grid.append(row)
        
    for i in range(N - 1, -1, -1):
        current_zeros = 0
        for seat in grid[i]:
            if seat == 0:
                current_zeros += 1
                if current_zeros >= A:
                    print(N - i)
                    return
            else:
                current_zeros = 0
                
    print(-1)

if __name__ == '__main__':
    solve()