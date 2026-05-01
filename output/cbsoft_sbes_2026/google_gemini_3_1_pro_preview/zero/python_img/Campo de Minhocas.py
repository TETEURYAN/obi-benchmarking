import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    matrix = []
    idx = 2
    for i in range(N):
        row = []
        for j in range(M):
            row.append(int(input_data[idx]))
            idx += 1
        matrix.append(row)
        
    max_sum = 0
    
    for i in range(N):
        current_sum = sum(matrix[i])
        if current_sum > max_sum:
            max_sum = current_sum
            
    for j in range(M):
        current_sum = sum(matrix[i][j] for i in range(N))
        if current_sum > max_sum:
            max_sum = current_sum
            
    print(max_sum)

if __name__ == '__main__':
    solve()