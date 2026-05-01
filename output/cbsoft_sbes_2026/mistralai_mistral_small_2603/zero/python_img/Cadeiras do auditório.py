
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return

    idx = 0
    L = int(data[idx])
    idx += 1
    C = int(data[idx])
    idx += 1

    grid = []
    for _ in range(L):
        row = list(map(int, data[idx:idx + C]))
        idx += C
        grid.append(row)

    original = [[(i * C + j + 1) for j in range(C)] for i in range(L)]

    row_ops = []
    col_ops = []

    current_grid = [row[:] for row in grid]

    for i in range(L):
        for j in range(C):
            if current_grid[i][j] != original[i][j]:
                target_val = original[i][j]
                found = False
                for x in range(i, L):
                    for y in range(C):
                        if current_grid[x][y] == target_val:
                            if x != i:
                                current_grid[x], current_grid[i] = current_grid[i], current_grid[x]
                                row_ops.append((i + 1, x + 1))
                            if y != j:
                                current_col = [current_grid[k][y] for k in range(L)]
                                for k in range(L):
                                    current_grid[k][y] = current_grid[k][j]
                                    current_grid[k][j] = current_col[k]
                                col_ops.append((j + 1, y + 1))
                            found = True
                            break
                    if found:
                        break

    total_ops = len(row_ops) + len(col_ops)
    print(total_ops)
    for op in row_ops:
        print(f"L {op[0]} {op[1]}")
    for op in col_ops:
        print(f"C {op[0]} {op[1]}")

if __name__ == "__main__":
    main()
