import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])
q = int(data[1])

row_time = [0] * (n + 1)
row_val = [0] * (n + 1)
col_time = [0] * (n + 1)
col_val = [0] * (n + 1)

out = []
t = 1
idx = 2

for _ in range(q):
    typ = int(data[idx])
    idx += 1

    if typ == 1:
        x = int(data[idx])
        r = int(data[idx + 1])
        idx += 2
        row_time[x] = t
        row_val[x] = r
        t += 1

    elif typ == 2:
        x = int(data[idx])
        r = int(data[idx + 1])
        idx += 2
        col_time[x] = t
        col_val[x] = r
        t += 1

    elif typ == 3:
        x = int(data[idx])
        idx += 1

        base_t = row_time[x]
        base_v = row_val[x]

        cnt = [0] * 51
        best_v = 0
        best_c = -1

        for j in range(1, n + 1):
            if col_time[j] > base_t:
                v = col_val[j]
            else:
                v = base_v
            cnt[v] += 1

        for v in range(51):
            c = cnt[v]
            if c > best_c or (c == best_c and v > best_v):
                best_c = c
                best_v = v

        out.append(str(best_v))

    else:
        x = int(data[idx])
        idx += 1

        base_t = col_time[x]
        base_v = col_val[x]

        cnt = [0] * 51
        best_v = 0
        best_c = -1

        for i in range(1, n + 1):
            if row_time[i] > base_t:
                v = row_val[i]
            else:
                v = base_v
            cnt[v] += 1

        for v in range(51):
            c = cnt[v]
            if c > best_c or (c == best_c and v > best_v):
                best_c = c
                best_v = v

        out.append(str(best_v))

sys.stdout.write("\n".join(out))