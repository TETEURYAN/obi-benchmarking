import sys
from collections import defaultdict, deque

def main():
    input = sys.stdin.readline

    L, C = map(int, input().split())

    rows = []
    row_sum = []
    var_rows = defaultdict(list)
    var_cols = defaultdict(list)
    vars_set = set()

    for i in range(L):
        parts = input().split()
        names = parts[:C]
        s = int(parts[C])
        rows.append(names)
        row_sum.append(s)
        for v in names:
            vars_set.add(v)
            var_rows[v].append(i)

    col_sum = list(map(int, input().split()))
    cols = [[] for _ in range(C)]
    for i in range(L):
        for j, v in enumerate(rows[i]):
            cols[j].append(v)
            var_cols[v].append(j)

    unknown_count_row = [0] * L
    unknown_count_col = [0] * C
    coeff_row = [defaultdict(int) for _ in range(L)]
    coeff_col = [defaultdict(int) for _ in range(C)]

    for i in range(L):
        d = coeff_row[i]
        for v in rows[i]:
            if d[v] == 0:
                unknown_count_row[i] += 1
            d[v] += 1

    for j in range(C):
        d = coeff_col[j]
        for v in cols[j]:
            if d[v] == 0:
                unknown_count_col[j] += 1
            d[v] += 1

    value = {}
    q = deque()

    for i in range(L):
        if unknown_count_row[i] == 1:
            q.append(('r', i))
    for j in range(C):
        if unknown_count_col[j] == 1:
            q.append(('c', j))

    while q and len(value) < len(vars_set):
        typ, idx = q.popleft()

        if typ == 'r':
            if unknown_count_row[idx] != 1:
                continue
            d = coeff_row[idx]
            target = row_sum[idx]
        else:
            if unknown_count_col[idx] != 1:
                continue
            d = coeff_col[idx]
            target = col_sum[idx]

        unknown_var = None
        coeff = 0
        for v, cnt in d.items():
            if v not in value:
                unknown_var = v
                coeff = cnt
                break

        if unknown_var is None:
            continue

        val = target // coeff
        value[unknown_var] = val

        for r in var_rows[unknown_var]:
            cnt = coeff_row[r].get(unknown_var, 0)
            if cnt:
                row_sum[r] -= cnt * val
                del coeff_row[r][unknown_var]
                unknown_count_row[r] -= 1
                if unknown_count_row[r] == 1:
                    q.append(('r', r))

        for c in var_cols[unknown_var]:
            cnt = coeff_col[c].get(unknown_var, 0)
            if cnt:
                col_sum[c] -= cnt * val
                del coeff_col[c][unknown_var]
                unknown_count_col[c] -= 1
                if unknown_count_col[c] == 1:
                    q.append(('c', c))

    out = []
    for v in sorted(value):
        out.append(f"{v} {value[v]}")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
