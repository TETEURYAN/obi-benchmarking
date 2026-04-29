import sys
from collections import deque, defaultdict

def main():
    input = sys.stdin.readline

    N, M = map(int, input().split())
    P = int(input())

    stones = set()
    cols = defaultdict(list)
    rows = defaultdict(list)

    for _ in range(P):
        c, l = map(int, input().split())
        stones.add((c, l))
        cols[c].append(l)
        rows[l].append(c)

    sc, sl = map(int, input().split())
    rc, rl = map(int, input().split())

    for c in cols:
        cols[c].sort()
    for l in rows:
        rows[l].sort()

    q = deque()
    visited = set()

    start = (sc, sl)
    target = (rc, rl)

    q.append(start)
    visited.add(start)

    while q:
        c, l = q.popleft()
        if (c, l) == target:
            print('S')
            return

        for nl in cols[c]:
            if nl == l:
                continue
            if abs(nl - l) <= 3 and (c, nl) not in visited:
                visited.add((c, nl))
                q.append((c, nl))

        for nc in rows[l]:
            if nc == c:
                continue
            if abs(nc - c) <= 3 and (nc, l) not in visited:
                visited.add((nc, l))
                q.append((nc, l))

    print('N')

if __name__ == "__main__":
    main()
