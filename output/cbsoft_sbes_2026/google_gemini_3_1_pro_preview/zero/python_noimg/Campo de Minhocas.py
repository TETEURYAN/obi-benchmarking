import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    matrix = []
    idx = 2
    for _ in range(N):
        row = []
        for _ in range(M):
            row.append(int(input_data[idx]))
            idx += 1
        matrix.append(row)
        
    max_sum = 0
    
    for row in matrix:
        row_sum = sum(row)
        if row_sum > max_sum:
            max_sum = row_sum
            
    for j in range(M):
        col_sum = sum(matrix[i][j] for i in range(N))
        if col_sum > max_sum:
            max_sum = col_sum
            
    print(max_sum)

if __name__ == '__main__':
    main()