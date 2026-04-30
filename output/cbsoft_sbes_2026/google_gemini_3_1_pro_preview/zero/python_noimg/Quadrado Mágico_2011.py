import sys

def solve():
    def get_ints():
        for line in sys.stdin:
            for token in line.split():
                yield int(token)
                
    tokens = get_ints()
    try:
        N = next(tokens)
    except StopIteration:
        return
        
    target_sum = N * (N * N + 1) // 2
    max_val = N * N
    seen = bytearray(max_val + 1)
    
    matrix = []
    for i in range(N):
        row = []
        row_sum = 0
        for j in range(N):
            val = next(tokens)
            if val < 1 or val > max_val or seen[val]:
                print(0)
                return
            seen[val] = 1
            row.append(val)
            row_sum += val
        if row_sum != target_sum:
            print(0)
            return
        matrix.append(row)
        
    for j in range(N):
        col_sum = 0
        for i in range(N):
            col_sum += matrix[i][j]
        if col_sum != target_sum:
            print(0)
            return
            
    diag1_sum = 0
    for i in range(N):
        diag1_sum += matrix[i][i]
    if diag1_sum != target_sum:
        print(0)
        return
        
    diag2_sum = 0
    for i in range(N):
        diag2_sum += matrix[i][N - 1 - i]
    if diag2_sum != target_sum:
        print(0)
        return
        
    print(target_sum)

if __name__ == '__main__':
    solve()