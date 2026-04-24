import sys

def main():
    data = sys.stdin.buffer.read().split()
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
        if op == b'L':
            row_perm[a], row_perm[b] = row_perm[b], row_perm[a]
        else:
            col_perm[a], col_perm[b] = col_perm[b], col_perm[a]
    
    # student at original row r, col c is r*M + c + 1
    # after permutations, position (i,j) has original row row_perm[i], col col_perm[j]
    out = []
    for i in range(N):
        r = row_perm[i]
        row_out = [r * M + col_perm[j] + 1 for j in range(M)]
        out.append(' '.join(map(str, row_out)))
    
    sys.stdout.write('\n'.join(out) + '\n')

main()