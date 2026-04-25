
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    idx = 0
    L = int(data[idx])
    C = int(data[idx + 1])
    idx += 2

    variables = []
    row_sums = []
    for _ in range(L):
        row = data[idx:idx + C]
        variables.extend(row[:-1])
        row_sum = int(row[-1])
        row_sums.append(row_sum)
        idx += C

    col_sums = list(map(int, data[idx:idx + C]))
    idx += C

    unique_vars = sorted(set(variables))
    var_to_idx = {var: i for i, var in enumerate(unique_vars)}
    n_vars = len(unique_vars)

    A = [[0] * n_vars for _ in range(L + C)]
    b = [0] * (L + C)

    for i in range(L):
        for j in range(C):
            var = data[2 + i * C + j]
            if var in var_to_idx:
                A[i][var_to_idx[var]] = 1
        b[i] = row_sums[i]

    for j in range(C):
        for i in range(L):
            var = data[2 + i * C + j]
            if var in var_to_idx:
                A[L + j][var_to_idx[var]] = 1
        b[L + j] = col_sums[j]

    solution = [0] * n_vars
    for i in range(L + C):
        if sum(A[i]) == 1:
            var_idx = next(j for j in range(n_vars) if A[i][j] == 1)
            solution[var_idx] = b[i]
            for k in range(L + C):
                if A[k][var_idx] == 1:
                    A[k][var_idx] = 0
                    b[k] -= solution[var_idx]

    for var in unique_vars:
        print(f"{var} {solution[var_to_idx[var]]}")

if __name__ == "__main__":
    main()
