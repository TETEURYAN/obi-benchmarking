import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    
    if n == 1:
        print(1)
        return
    
    if n == 2:
        print(-1)
        return
        
    if n % 2 == 1:
        # Odd case: sequential filling
        # Row i contains i*N + 1, ..., i*N + N
        # Sum is N*(first + last)/2 = N*(2*i*N + 1 + N)/2
        # Avg is (i*N + (N+1)/2), which is the middle element.
        # Columns also work similarly.
        out = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(str(i * n + j + 1))
            out.append(" ".join(row))
        print("\n".join(out))
        return
    
    # Even case N >= 4
    # Construct using offsets
    # R = N/2, C = N/2
    r = n // 2
    c = n // 2
    
    # Generate row offsets
    # O_R[c] = 0
    # Others: 1, 2, ..., N-2 and -(N-2)(N-1)/2
    row_offsets = [0] * n
    # Indices other than c
    indices = [i for i in range(n) if i != c]
    
    # Assign positive offsets
    for k in range(n - 2):
        row_offsets[indices[k]] = k + 1
        
    # Assign negative offset
    # Sum of 1..N-2 is (N-2)(N-1)/2
    neg_val = (n - 2) * (n - 1) // 2
    row_offsets[indices[n - 2]] = -neg_val
    
    # Generate col offsets
    # Scaled by N^2 to ensure distinctness
    # O_C[r] = 0
    # Others: S, 2S, ... and -Sum*S
    S = n * n
    col_offsets = [0] * n
    indices_c = [i for i in range(n) if i != r]
    
    for k in range(n - 2):
        col_offsets[indices_c[k]] = (k + 1) * S
        
    col_offsets[indices_c[n - 2]] = -neg_val * S
    
    # Base value
    # Min value occurs at min(row_offsets) + min(col_offsets)
    # min(row_offsets) approx -N^2/2
    # min(col_offsets) approx -N^3/2
    # We need V + min > 0
    # V = N^3 is safe
    V = n * n * n
    
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = V + col_offsets[i] + row_offsets[j]
            
    out = []
    for i in range(n):
        out.append(" ".join(map(str, matrix[i])))
    print("\n".join(out))

if __name__ == '__main__':
    solve()