import sys
import bisect

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx])
idx += 1
Q = int(input_data[idx])
idx += 1

last_row_time = [0] * (N + 1)
row_val = [0] * (N + 1)
last_col_time = [0] * (N + 1)
col_val = [0] * (N + 1)
row_ops = [None] * (Q + 1)
col_ops = [None] * (Q + 1)
row_freq_lists = [[] for _ in range(51)]
col_freq_lists = [[] for _ in range(51)]
prefix_row = [0] * (Q + 2)
prefix_col = [0] * (Q + 2)

for t in range(1, Q + 1):
    op_type = int(input_data[idx])
    idx += 1
    if op_type == 1:
        X = int(input_data[idx])
        idx += 1
        R = int(input_data[idx])
        idx += 1
        last_row_time[X] = t
        row_val[X] = R
        row_ops[t] = (X, R)
        row_freq_lists[R].append(t)
        prefix_row[t] = prefix_row[t - 1] + 1
        prefix_col[t] = prefix_col[t - 1]
    elif op_type == 2:
        X = int(input_data[idx])
        idx += 1
        R = int(input_data[idx])
        idx += 1
        last_col_time[X] = t
        col_val[X] = R
        col_ops[t] = (X, R)
        col_freq_lists[R].append(t)
        prefix_col[t] = prefix_col[t - 1] + 1
        prefix_row[t] = prefix_row[t - 1]
    elif op_type == 3:
        X = int(input_data[idx])
        idx += 1
        rt = last_row_time[X]
        rv = row_val[X]
        freq = [0] * 51
        num_eq = 1 if rt > 0 and col_ops[rt] is not None else 0
        num_greater = prefix_col[t - 1] - prefix_col[rt]
        num_less = N - num_eq - num_greater
        if num_less > 0:
            freq[rv] += num_less
        for val in range(51):
            if col_freq_lists[val]:
                idx_b = bisect.bisect_left(col_freq_lists[val], rt + 1)
                count = len(col_freq_lists[val]) - idx_b
                freq[val] += count
        if rt == 0:
            num_zero = N - num_greater
            freq[0] += num_zero
        else:
            freq[0] += num_eq
        max_f = max(freq)
        candidates = [v for v in range(51) if freq[v] == max_f]
        print(max(candidates))
        prefix_row[t] = prefix_row[t - 1]
        prefix_col[t] = prefix_col[t - 1]
    elif op_type == 4:
        X = int(input_data[idx])
        idx += 1
        ct = last_col_time[X]
        cv = col_val[X]
        freq = [0] * 51
        num_eq = 1 if ct > 0 and row_ops[ct] is not None else 0
        num_greater = prefix_row[t - 1] - prefix_row[ct]
        num_less = N - num_eq - num_greater
        if num_less > 0:
            freq[cv] += num_less
        for val in range(51):
            if row_freq_lists[val]:
                idx_b = bisect.bisect_left(row_freq_lists[val], ct + 1)
                count = len(row_freq_lists[val]) - idx_b
                freq[val] += count
        if ct == 0:
            num_zero = N - num_greater
            freq[0] += num_zero
        else:
            freq[0] += num_eq
        max_f = max(freq)
        candidates = [v for v in range(51) if freq[v] == max_f]
        print(max(candidates))
        prefix_row[t] = prefix_row[t - 1]
        prefix_col[t] = prefix_col[t - 1]