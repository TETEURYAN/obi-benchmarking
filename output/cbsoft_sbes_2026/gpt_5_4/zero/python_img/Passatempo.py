import sys
from collections import defaultdict, deque

def main():
    input = sys.stdin.readline
    L, C = map(int, input().split())

    row_sum = [0] * L
    col_sum = [0] * C

    row_count = [defaultdict(int) for _ in range(L)]
    col_count = [defaultdict(int) for _ in range(C)]

    var_rows = defaultdict(list)
    var_cols = defaultdict(list)
    vars_set = set()

    for i in range(L):
        parts = input().split()
        names = parts[:C]
        s = int(parts[C])
        row_sum[i] = s
        for name in names:
            row_count[i][name] += 1
            vars_set.add(name)
        for name in row_count[i]:
            var_rows[name].append(i)

    xs = list(map(int, input().split()))
    for j in range(C):
        col_sum[j] = xs[j]

    grid_rows = []
    sys.stdin.seek if False else None

    # Re-read impossible, so build columns from stored rows not available.
    # Instead, reconstruct by reading was not stored; thus store while reading above.
    # To keep structure simple, parse again is impossible, so let's rebuild from row_count only not enough for columns.
    # Therefore store rows during input.
def solve():
    input = sys.stdin.readline
    L, C = map(int, input().split())

    row_sum = [0] * L
    col_sum = [0] * C

    row_count = [defaultdict(int) for _ in range(L)]
    col_count = [defaultdict(int) for _ in range(C)]

    var_rows = defaultdict(list)
    var_cols = defaultdict(list)
    vars_set = set()

    rows_names = []

    for i in range(L):
        parts = input().split()
        names = parts[:C]
        rows_names.append(names)
        s = int(parts[C])
        row_sum[i] = s
        for name in names:
            row_count[i][name] += 1
            vars_set.add(name)
        for name in row_count[i]:
            var_rows[name].append(i)

    xs = list(map(int, input().split()))
    for j in range(C):
        col_sum[j] = xs[j]

    for i in range(L):
        for j, name in enumerate(rows_names[i]):
            col_count[j][name] += 1

    for j in range(C):
        for name in col_count[j]:
            var_cols[name].append(j)

    unresolved_row = [len(row_count[i]) for i in range(L)]
    unresolved_col = [len(col_count[j]) for j in range(C)]

    q = deque()
    in_queue_row = [False] * L
    in_queue_col = [False] * C

    for i in range(L):
        if unresolved_row[i] == 1:
            q.append(('r', i))
            in_queue_row[i] = True
    for j in range(C):
        if unresolved_col[j] == 1:
            q.append(('c', j))
            in_queue_col[j] = True

    value = {}

    while q:
        typ, idx = q.popleft()

        if typ == 'r':
            if unresolved_row[idx] != 1:
                continue
            for name, cnt in row_count[idx].items():
                if name not in value:
                    v = row_sum[idx] // cnt
                    value[name] = v
                    break
        else:
            if unresolved_col[idx] != 1:
                continue
            for name, cnt in col_count[idx].items():
                if name not in value:
                    v = col_sum[idx] // cnt
                    value[name] = v
                    break

        if name in value:
            v = value[name]

            for r in var_rows[name]:
                cnt = row_count[r].pop(name, 0)
                if cnt:
                    row_sum[r] -= cnt * v
                    unresolved_row[r] -= 1
                    if unresolved_row[r] == 1:
                        q.append(('r', r))

            for c in var_cols[name]:
                cnt = col_count[c].pop(name, 0)
                if cnt:
                    col_sum[c] -= cnt * v
                    unresolved_col[c] -= 1
                    if unresolved_col[c] == 1:
                        q.append(('c', c))

    for name in sorted(value):
        print(name, value[name])

solve()