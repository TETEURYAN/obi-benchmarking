
import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().split()
    ptr = 0
    L = int(data[ptr])
    C = int(data[ptr+1])
    ptr += 2

    variables = []
    sums_rows = []
    for _ in range(L):
        row = []
        while len(row) < C + 1:
            row.append(data[ptr])
            ptr += 1
        variables_row = row[:C]
        sum_row = int(row[C])
        variables.append(variables_row)
        sums_rows.append(sum_row)

    sums_cols = list(map(int, data[ptr:ptr+C]))
    ptr += C

    var_to_row = defaultdict(list)
    var_to_col = defaultdict(list)
    for i in range(L):
        for j in range(C):
            var = variables[i][j]
            var_to_row[var].append(i)
            var_to_col[var].append(j)

    known = {}
    while len(known) < len(var_to_row):
        progress = False
        for var in sorted(var_to_row.keys()):
            if var in known:
                continue
            rows = var_to_row[var]
            cols = var_to_col[var]
            row_sums = []
            for i in rows:
                sum_val = sums_rows[i]
                for j in range(C):
                    other_var = variables[i][j]
                    if other_var != var and other_var not in known:
                        break
                else:
                    row_sums.append(sum_val)
            if len(row_sums) == 1:
                sum_val = row_sums[0]
                for j in cols:
                    for i in range(L):
                        other_var = variables[i][j]
                        if other_var != var and other_var not in known:
                            break
                    else:
                        col_sum = sums_cols[j]
                        sum_val -= col_sum - known.get(other_var, 0)
                known[var] = sum_val
                progress = True
                break

            col_sums = []
            for j in cols:
                sum_val = sums_cols[j]
                for i in range(L):
                    other_var = variables[i][j]
                    if other_var != var and other_var not in known:
                        break
                else:
                    col_sums.append(sum_val)
            if len(col_sums) == 1:
                sum_val = col_sums[0]
                for i in rows:
                    sum_row = sums_rows[i]
                    for j in range(C):
                        other_var = variables[i][j]
                        if other_var != var and other_var not in known:
                            break
                    else:
                        sum_val -= sum_row - known.get(other_var, 0)
                known[var] = sum_val
                progress = True
                break
        if not progress:
            break

    for var in sorted(known.keys()):
        print(f"{var} {known[var]}")

if __name__ == "__main__":
    main()
