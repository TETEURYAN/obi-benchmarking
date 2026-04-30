import sys
input = sys.stdin.readline

def main():
    import sys
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx+=1
    M = int(data[idx]); idx+=1
    P = int(data[idx]); idx+=1
    
    # row_perm[i] = which original row is now at position i (0-indexed)
    row_perm = list(range(N))
    col_perm = list(range(M))
    
    for _ in range(P):
        op = data[idx]; idx+=1
        a = int(data[idx])-1; idx+=1
        b = int(data[idx])-1; idx+=1
        if op == 'L':
            row_perm[a], row_perm[b] = row_perm[b], row_perm[a]
        else:
            col_perm[a], col_perm[b] = col_perm[b], col_perm[a]
    
    # Student at original row r, col c has number r*M + c + 1
    # After permutations, position (i,j) has original row row_perm[i], original col col_perm[j]
    # So student number = row_perm[i]*M + col_perm[j] + 1
    
    out = []
    for i in range(N):
        r = row_perm[i]
        base = r * M + 1
        row_out = [base + col_perm[j] for j in range(M)]
        out.append(' '.join(map(str, row_out)))
    
    sys.stdout.write('\n'.join(out) + '\n')

main()