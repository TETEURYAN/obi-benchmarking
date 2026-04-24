import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    matrix = []
    idx = 1
    for i in range(n):
        matrix.append([int(x) for x in input_data[idx:idx+n]])
        idx += n
        
    row_sums = [sum(row) for row in matrix]
    col_sums = [sum(matrix[i][j] for i in range(n)) for j in range(n)]
    
    max_weight = 0
    for i in range(n):
        for j in range(n):
            weight = row_sums[i] + col_sums[j] - 2 * matrix[i][j]
            if weight > max_weight:
                max_weight = weight
                
    print(max_weight)

if __name__ == '__main__':
    solve()