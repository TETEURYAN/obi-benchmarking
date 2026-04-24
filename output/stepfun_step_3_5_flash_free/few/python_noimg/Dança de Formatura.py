import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    P = int(next(it))
    
    row_perm = list(range(N+1))
    col_perm = list(range(M+1))
    
    for _ in range(P):
        op = next(it)
        a = int(next(it))
        b = int(next(it))
        if op == 'L':
            row_perm[a], row_perm[b] = row_perm[b], row_perm[a]
        else:
            col_perm[a], col_perm[b] = col_perm[b], col_perm[a]
    
    output_lines = []
    for i in range(1, N+1):
        base = (row_perm[i] - 1) * M
        line = [str(base + col_perm[j]) for j in range(1, M+1)]
        output_lines.append(' '.join(line))
    
    sys.stdout.write('\n'.join(output_lines))

if __name__ == '__main__':
    main()