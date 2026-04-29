import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    it = iter(data)
    n = int(next(it))
    a = [[int(next(it)) for _ in range(n)] for _ in range(n)]
    
    row_sums = [sum(row) for row in a]
    col_sums = [sum(a[i][j] for i in range(n)) for j in range(n)]
    
    def find_magic_sum(sums):
        if sums[0] == sums[1] or sums[0] == sums[2]:
            return sums[0]
        return sums[1]
    
    M = find_magic_sum(row_sums)
    
    bad_row = -1
    for i in range(n):
        if row_sums[i] != M:
            bad_row = i
            break
    
    bad_col = -1
    for j in range(n):
        if col_sums[j] != M:
            bad_col = j
            break
    
    changed = a[bad_row][bad_col]
    original = changed + (M - row_sums[bad_row])
    
    print(original, changed)

if __name__ == "__main__":
    main()
