
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    P = int(input_data[2])
    
    row_perm = list(range(N))
    col_perm = list(range(M))
    
    idx = 3
    for _ in range(P):
        op = input_data[idx]
        a = int(input_data[idx+1]) - 1
        b = int(input_data[idx+2]) - 1
        idx += 3
        
        if op == 'L':
            row_perm[a], row_perm[b] = row_perm[b], row_perm[a]
        else:
            col_perm[a], col_perm[b] = col_perm[b], col_perm[a]
            
    col_vals = [c + 1 for c in col_perm]
    
    for i in range(N):
        base = row_perm[i] * M
        sys.stdout.write(" ".join(str(base + cv) for cv in col_vals) + "\n")

if __name__ == '__main__':
    solve()
