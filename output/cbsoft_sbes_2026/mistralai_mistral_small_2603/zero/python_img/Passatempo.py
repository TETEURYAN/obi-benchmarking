
import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return

    L, C = map(int, data[0].split())
    grid = []
    sums_rows = []
    variables = set()

    for i in range(1, L + 1):
        parts = data[i].split()
        row_vars = parts[:C]
        sum_row = int(parts[C])
        grid.append(row_vars)
        sums_rows.append(sum_row)
        for var in row_vars:
            variables.add(var)

    sums_cols = list(map(int, data[L + 1].split()))

    var_to_value = {}
    remaining_vars = set(variables)

    while remaining_vars:
        found = False
        for i in range(L):
            row = grid[i]
            sum_row = sums_rows[i]
            unknowns = [var for var in row if var in remaining_vars]
            if len(unknowns) == 1:
                var = unknowns[0]
                total_known = sum_row - sum(var_to_value.get(v, 0) for v in row if v != var)
                var_to_value[var] = total_known
                remaining_vars.remove(var)
                found = True
                break

        if not found:
            for j in range(C):
                col = [grid[i][j] for i in range(L)]
                sum_col = sums_cols[j]
                unknowns = [var for var in col if var in remaining_vars]
                if len(unknowns) == 1:
                    var = unknowns[0]
                    total_known = sum_col - sum(var_to_value.get(v, 0) for v in col if v != var)
                    var_to_value[var] = total_known
                    remaining_vars.remove(var)
                    found = True
                    break

        if not found:
            break

    sorted_vars = sorted(remaining_vars)
    for var in sorted_vars:
        if var not in var_to_value:
            for i in range(L):
                row = grid[i]
                sum_row = sums_rows[i]
                unknowns = [v for v in row if v in remaining_vars]
                if len(unknowns) == 1:
                    v = unknowns[0]
                    total_known = sum_row - sum(var_to_value.get(u, 0) for u in row if u != v)
                    var_to_value[v] = total_known
                    remaining_vars.remove(v)
                    break
            else:
                for j in range(C):
                    col = [grid[i][j] for i in range(L)]
                    sum_col = sums_cols[j]
                    unknowns = [v for v in col if v in remaining_vars]
                    if len(unknowns) == 1:
                        v = unknowns[0]
                        total_known = sum_col - sum(var_to_value.get(u, 0) for u in col if u != v)
                        var_to_value[v] = total_known
                        remaining_vars.remove(v)
                        break

    for var in sorted(variables):
        print(f"{var} {var_to_value[var]}")

if __name__ == "__main__":
    main()
