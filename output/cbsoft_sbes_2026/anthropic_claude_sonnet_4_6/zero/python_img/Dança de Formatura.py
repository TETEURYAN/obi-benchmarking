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
    
    out = []
    for i in range(N):
        r = row_perm[i]
        row_out = []
        for j in range(M):
            c = col_perm[j]
            # original student at (r, c) is r*M + c + 1
            row_out.append(r * M + c + 1)
        out.append(' '.join(map(str, row_out)))
    
    sys.stdout.write('\n'.join(out) + '\n')

main()