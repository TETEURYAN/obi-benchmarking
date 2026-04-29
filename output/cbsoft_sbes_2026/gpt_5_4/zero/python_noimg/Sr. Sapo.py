import sys
from collections import deque, defaultdict

def main():
    input = sys.stdin.readline

    N, M = map(int, input().split())
    P = int(input())

    stones = []
    row_to_cols = defaultdict(list)
    col_to_rows = defaultdict(list)

    for _ in range(P):
        c, l = map(int, input().split())
        stones.append((c, l))
        row_to_cols[l].append(c)
        col_to_rows[c].append(l)

    sc, sl = map(int, input().split())
    rc, rl = map(int, input().split())

    for l in row_to_cols:
        row_to_cols[l].sort()
    for c in col_to_rows:
        col_to_rows[c].sort()

    start = (sc, sl)
    target = (rc, rl)

    q = deque([start])
    visited = {start}

    while q:
        c, l = q.popleft()
        if (c, l) == target:
            print('S')
            return

        cols = row_to_cols[l]
        for nc in cols:
            if nc == c:
                continue
            if abs(nc - c) <= 3:
                nxt = (nc, l)
                if nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)

        rows = col_to_rows[c]
        for nl in rows:
            if nl == l:
                continue
            if abs(nl - l) <= 3:
                nxt = (c, nl)
                if nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)

    print('N')

if __name__ == "__main__":
    main()
