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
    
    # Chair number (i,j) should be (i-1)*C + j (1-indexed)
    # Given grid[i][j] = chair number at position (i+1, j+1)
    # We need to find row permutation and column permutation
    
    # For each chair number n, its original position is:
    # orig_row = (n-1) // C  (0-indexed)
    # orig_col = (n-1) % C   (0-indexed)
    
    # After row and column permutations, grid[i][j] = chair at (row_perm[i], col_perm[j]) originally
    # So grid[i][j] = row_perm[i] * C + col_perm[j] + 1
    
    # First, determine row permutation from first column
    # grid[i][0] = row_perm[i] * C + col_perm[0] + 1
    # grid[i][j] - grid[i][0] = col_perm[j] - col_perm[0] (constant for each row)
    
    # Determine row_perm: from any column, grid[i][j] gives orig_row = (grid[i][j]-1)//C
    # But this only works if columns are permuted consistently
    # Actually: orig_row of chair at (i,j) = (grid[i][j]-1)//C = row_perm[i]
    # This should be same for all j in row i
    
    row_perm = []
    for i in range(L):
        row_perm.append((grid[i][0] - 1) // C)
    
    col_perm = []
    for j in range(C):
        col_perm.append((grid[0][j] - 1) % C)
    
    # Now we need to sort row_perm to [0,1,...,L-1] and col_perm to [0,1,...,C-1]
    # using minimum swaps (selection sort gives at most n-1 swaps)
    
    ops = []
    
    # Sort row_perm using selection sort
    rp = list(row_perm)
    # rp[i] should become i
    # Create inverse: pos[v] = current index of value v
    pos = [0] * L
    for i in range(L):
        pos[rp[i]] = i
    
    for i in range(L):
        if rp[i] != i:
            # find where i is
            j = pos[i]
            # swap rp[i] and rp[j]
            ops.append(('L', i+1, j+1))
            pos[rp[i]] = j
            pos[i] = i
            rp[i], rp[j] = rp[j], rp[i]
    
    # Sort col_perm using selection sort
    cp = list(col_perm)
    pos2 = [0] * C
    for i in range(C):
        pos2[cp[i]] = i
    
    for i in range(C):
        if cp[i] != i:
            j = pos2[i]
            ops.append(('C', i+1, j+1))
            pos2[cp[i]] = j
            pos2[i] = i
            cp[i], cp[j] = cp[j], cp[i]
    
    print(len(ops))
    for op in ops:
        print(op[0], op[1], op[2])

solve()