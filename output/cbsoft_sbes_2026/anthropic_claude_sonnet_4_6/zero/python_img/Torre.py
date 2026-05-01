import sys
input = sys.stdin.readline

def main():
    n = int(input())
    grid = []
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)
    
    row_sums = [sum(grid[i]) for i in range(n)]
    col_sums = [sum(grid[i][j] for i in range(n)) for j in range(n)]
    
    max_weight = 0
    for i in range(n):
        for j in range(n):
            weight = row_sums[i] + col_sums[j] - grid[i][j]
            if weight > max_weight:
                max_weight = weight
    
    print(max_weight)

main()