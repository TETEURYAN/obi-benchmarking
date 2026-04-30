
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    L = int(input_data[0])
    C = int(input_data[1])
    
    grid = []
    idx = 2
    for i in range(L):
        row = []
        for j in range(C):
            row.append(int(input_data[idx]))
            idx += 1
        grid.append(row)
        
    row_perm = [(grid[i][0] - 1) // C for i in range(L)]
    col_perm = [(grid[0][j] - 1) % C for j in range(C)]
    
    swaps = []
    
    for i in range(L):
        if row_perm[i] != i:
            k = i + 1
            while k < L and row_perm[k] != i:
                k += 1
            row_perm[i], row_perm[k] = row_perm[k], row_perm[i]
            swaps.append(('L', i + 1, k + 1))
            
    for j in range(C):
        if col_perm[j] != j:
            k = j + 1
            while k < C and col_perm[k] != j:
                k += 1
            col_perm[j], col_perm[k] = col_perm[k], col_perm[j]
            swaps.append(('C', j + 1, k + 1))
            
    print(len(swaps))
    for swap in swaps:
        print(f"{swap[0]} {swap[1]} {swap[2]}")

if __name__ == '__main__':
    solve()
