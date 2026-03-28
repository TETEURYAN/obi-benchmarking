
import sys
sys.setrecursionlimit(1 << 25)

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    N = int(data[0])
    M = int(data[1])
    total_cells = N * M
    powers = list(map(int, data[2:]))
    
    cells = []
    for i in range(N):
        for j in range(M):
            idx = i * M + j
            cells.append((powers[idx], i, j))
    
    cells.sort()
    
    ans = [0] * total_cells
    max_in_row = [0] * N
    max_in_col = [0] * M
    
    pos_dict = {}
    for i, (p, r, c) in enumerate(cells):
        pos_dict[(r, c)] = i
    
    for i in range(total_cells):
        p, r, c = cells[i]
        best = p
        if r > 0:
            idx_above = pos_dict.get((r-1, c))
            if idx_above is not None and idx_above < i:
                best = max(best, ans[idx_above] + p)
        if r < N-1:
            idx_below = pos_dict.get((r+1, c))
            if idx_below is not None and idx_below < i:
                best = max(best, ans[idx_below] + p)
        if c > 0:
            idx_left = pos_dict.get((r, c-1))
            if idx_left is not None and idx_left < i:
                best = max(best, ans[idx_left] + p)
        if c < M-1:
            idx_right = pos_dict.get((r, c+1))
            if idx_right is not None and idx_right < i:
                best = max(best, ans[idx_right] + p)
        ans[i] = best
        max_in_row[r] = max(max_in_row[r], best)
        max_in_col[c] = max(max_in_col[c], best)
    
    for i in range(total_cells):
        p, r, c = cells[i]
        if ans[i] < max_in_row[r] + p:
            ans[i] = max_in_row[r] + p
        if ans[i] < max_in_col[c] + p:
            ans[i] = max_in_col[c] + p
    
    output_lines = []
    for i in range(N):
        line = []
        for j in range(M):
            idx = pos_dict[(i, j)]
            line.append(str(ans[idx]))
        output_lines.append(' '.join(line))
    
    sys.stdout.write('\n'.join(output_lines))

if __name__ == "__main__":
    solve()
