
import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    it = iter(data)
    N = int(next(it))
    Q = int(next(it))

    row_val = [0] * (N + 1)
    col_val = [0] * (N + 1)
    row_time = [0] * (N + 1)
    col_time = [0] * (N + 1)
    current_time = 0

    freq_row = [defaultdict(int) for _ in range(N + 1)]
    freq_col = [defaultdict(int) for _ in range(N + 1)]
    max_freq_row = [0] * (N + 1)
    max_freq_col = [0] * (N + 1)
    best_val_row = [0] * (N + 1)
    best_val_col = [0] * (N + 1)

    output = []

    for _ in range(Q):
        op = int(next(it))
        if op == 1:
            X = int(next(it))
            R = int(next(it))
            current_time += 1
            old_val = row_val[X]
            if old_val != 0:
                freq_row[X][old_val] -= 1
                if freq_row[X][old_val] == 0:
                    del freq_row[X][old_val]
            row_val[X] = R
            row_time[X] = current_time
            freq_row[X][R] += 1
            if freq_row[X][R] > max_freq_row[X]:
                max_freq_row[X] = freq_row[X][R]
                best_val_row[X] = R
            elif freq_row[X][R] == max_freq_row[X]:
                if R > best_val_row[X]:
                    best_val_row[X] = R
        elif op == 2:
            X = int(next(it))
            R = int(next(it))
            current_time += 1
            old_val = col_val[X]
            if old_val != 0:
                freq_col[X][old_val] -= 1
                if freq_col[X][old_val] == 0:
                    del freq_col[X][old_val]
            col_val[X] = R
            col_time[X] = current_time
            freq_col[X][R] += 1
            if freq_col[X][R] > max_freq_col[X]:
                max_freq_col[X] = freq_col[X][R]
                best_val_col[X] = R
            elif freq_col[X][R] == max_freq_col[X]:
                if R > best_val_col[X]:
                    best_val_col[X] = R
        elif op == 3:
            X = int(next(it))
            if row_time[X] == 0:
                output.append("0")
            else:
                output.append(str(best_val_row[X]))
        elif op == 4:
            X = int(next(it))
            if col_time[X] == 0:
                output.append("0")
            else:
                output.append(str(best_val_col[X]))

    print('\n'.join(output))

if __name__ == "__main__":
    main()
