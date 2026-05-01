import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    L = int(input_data[idx]); idx += 1
    C = int(input_data[idx]); idx += 1
    
    grid = []
    for i in range(L):
        row = []
        for j in range(C):
            row.append(int(input_data[idx])); idx += 1
        grid.append(row)
    
    # Chair number at position (i,j) in original: (i)*C + (j+1) = i*C + j + 1
    # Chair number chair_num is originally at row (chair_num-1)//C, col (chair_num-1)%C (0-indexed)
    
    # We need to find row permutation and column permutation such that
    # grid[row_perm[i]][col_perm[j]] == i*C + j + 1 for all i,j
    # i.e., the chair at position (row_perm[i], col_perm[j]) in current grid is the original chair for (i,j)
    
    # Actually, let's think differently:
    # grid[i][j] = chair number currently at position (i,j)
    # Original position of chair number n is row (n-1)//C, col (n-1)%C (0-indexed)
    # We need swaps of rows/cols to restore original arrangement
    
    # The current grid is a permutation of rows and columns of the original.
    # Let's find row_perm and col_perm (0-indexed):
    # grid[i][j] = (row_perm[i]) * C + col_perm[j] + 1
    # So row_perm[i] = (grid[i][0] - 1) // C  (using column 0)
    # col_perm[j] = (grid[0][j] - 1) % C  (using row 0)
    
    # Verify this is consistent
    row_perm = []
    for i in range(L):
        row_perm.append((grid[i][0] - 1) // C)
    
    col_perm = []
    for j in range(C):
        col_perm.append((grid[0][j] - 1) % C)
    
    # Now we need to sort row_perm to [0,1,...,L-1] using swaps -> minimum swaps via selection sort
    # and col_perm to [0,1,...,C-1] using swaps
    
    moves = []
    
    # Sort row_perm using selection sort (minimum swaps for a permutation)
    # row_perm[i] should become i
    # We need to track where each value is
    pos = list(range(L))  # pos[v] = current index where value v is
    for i in range(L):
        pos[row_perm[i]] = i
    
    for i in range(L):
        if row_perm[i] != i:
            # Find where value i is
            j = pos[i]
            # Swap positions i and j in row_perm
            # Update pos
            pos[row_perm[i]] = j
            pos[i] = i
            row_perm[i], row_perm[j] = row_perm[j], row_perm[i]
            moves.append(('L', i+1, j+1))
    
    # Sort col_perm
    pos2 = list(range(C))
    for j in range(C):
        pos2[col_perm[j]] = j
    
    for j in range(C):
        if col_perm[j] != j:
            k = pos2[j]
            pos2[col_perm[j]] = k
            pos2[j] = j
            col_perm[j], col_perm[k] = col_perm[k], col_perm[j]
            moves.append(('C', j+1, k+1))
    
    print(len(moves))
    for m in moves:
        print(m[0], m[1], m[2])

solve()