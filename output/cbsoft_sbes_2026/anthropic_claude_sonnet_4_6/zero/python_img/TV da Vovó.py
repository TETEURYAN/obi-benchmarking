import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    test_num = 0
    results = []
    
    while idx < len(input_data):
        M = int(input_data[idx]); N = int(input_data[idx+1])
        idx += 2
        
        if M == 0 and N == 0:
            break
        
        test_num += 1
        
        # Read M rows, each with N integers
        matrix = []
        for i in range(M):
            row = []
            for j in range(N):
                row.append(int(input_data[idx]))
                idx += 1
            matrix.append(row)
        
        # Accumulate total shift
        total_x = 0  # horizontal shift (positive = right)
        total_y = 0  # vertical shift (positive = up)
        
        while idx < len(input_data):
            X = int(input_data[idx]); Y = int(input_data[idx+1])
            idx += 2
            if X == 0 and Y == 0:
                break
            total_x += X
            total_y += Y
        
        # Apply shifts
        # X positive = shift right: column j in result comes from column (j - total_x) % N
        # Y positive = shift up: row i in result comes from row (i + total_y) % M
        
        col_shift = total_x % N
        row_shift = (-total_y) % M  # shift up by total_y means row i comes from (i + total_y) % M
        # Actually: shift up by total_y means image moves up, so row i in result = row (i + total_y) % M
        # row_shift for indexing: source_row = (i + total_y) % M
        
        result = []
        for i in range(M):
            src_row = (i + total_y) % M
            row = []
            for j in range(N):
                src_col = (j - total_x) % N
                row.append(matrix[src_row][src_col])
            result.append(row)
        
        out = []
        out.append(f"Teste {test_num}")
        for row in result:
            out.append(' '.join(map(str, row)) + ' ')
        out.append('')
        results.append('\n'.join(out))
    
    print('\n'.join(results))

solve()