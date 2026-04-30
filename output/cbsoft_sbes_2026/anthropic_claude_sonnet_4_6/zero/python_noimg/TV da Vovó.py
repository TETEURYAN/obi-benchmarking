import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    test_num = 1
    
    while idx < len(input_data):
        M = int(input_data[idx]); N = int(input_data[idx+1])
        idx += 2
        
        if M == 0 and N == 0:
            break
        
        # Read M lines, each with N integers
        matrix = []
        for i in range(M):
            row = []
            for j in range(N):
                row.append(int(input_data[idx]))
                idx += 1
            matrix.append(row)
        
        # Total row shift and col shift
        total_row_shift = 0  # positive = down, negative = up
        total_col_shift = 0  # positive = right, negative = left
        
        # Read commands until 0 0
        while idx < len(input_data):
            X = int(input_data[idx]); Y = int(input_data[idx+1])
            idx += 2
            if X == 0 and Y == 0:
                break
            # X: positive = right (col shift), negative = left
            # Y: positive = up (row shift negative), negative = down (row shift positive)
            total_col_shift += X
            total_row_shift += (-Y)  # positive Y means up, which means rows shift up (negative row shift)
        
        # Apply shifts
        # row shift: total_row_shift > 0 means image moved down, so content shifts down
        # Actually let's think carefully:
        # Y positive = up: image moves up, so row index decreases
        # row_shift = -Y means: if Y=1 (up), row_shift = -1
        # The new matrix[i][j] = old matrix[(i - row_shift) % M][(j - col_shift) % N]
        # Wait, let's think again:
        # If image shifts up by 1 (Y=1), row 0 of new image = row 1 of old image
        # new[i][j] = old[i + row_shift_up][j]
        # row_shift_up = Y (positive = up)
        # col_shift_right = X (positive = right)
        # If image shifts right by 1, col 0 of new = col (N-1) of old
        # new[i][j] = old[i][j - col_shift_right]
        
        # So: new[i][j] = old[(i + total_Y) % M][(j - total_X) % N]
        # where total_Y = sum of Y values, total_X = sum of X values
        
        # Let me recompute:
        # total_col_shift = sum of X (right shifts)
        # total_row_shift = sum of -Y (but let's use total_Y = sum of Y)
        
        # Recompute properly
        # I stored total_row_shift = sum(-Y) = -sum(Y)
        # total_col_shift = sum(X)
        
        # new[i][j] = old[(i - (-total_row_shift)) % M][(j - total_col_shift) % N]
        # = old[(i + total_row_shift) % M]... wait
        
        # total_row_shift = sum(-Y)
        # new[i][j] = old[(i + sum(Y)) % M][(j - sum(X)) % N]
        # = old[(i - total_row_shift) % M][(j - total_col_shift) % N]
        
        total_Y = -total_row_shift  # sum of Y
        total_X = total_col_shift   # sum of X
        
        result = []
        for i in range(M):
            row = []
            for j in range(N):
                old_i = (i + total_Y) % M
                old_j = (j - total_X) % N
                row.append(matrix[old_i][old_j])
            result.append(row)
        
        print(f"Teste {test_num}")
        for i in range(M):
            print(' '.join(map(str, result[i])) + ' ')
        print()
        test_num += 1

solve()