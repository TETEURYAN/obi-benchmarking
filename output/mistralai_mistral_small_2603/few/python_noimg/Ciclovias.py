
import sys
from bisect import bisect_left

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    for i in range(1, n + 1):
        adj[i].sort()

    dp_inc = [1] * (n + 1)
    dp_dec = [1] * (n + 1)

    for u in range(1, n + 1):
        for v in adj[u]:
            if v > u:
                pos = bisect_left(adj[v], u)
                if pos > 0:
                    dp_inc[v] = max(dp_inc[v], dp_inc[adj[v][pos - 1]] + 1)
            if v < u:
                pos = bisect_left(adj[v], u)
                if pos < len(adj[v]) - 1:
                    dp_dec[v] = max(dp_dec[v], dp_dec[adj[v][pos + 1]] + 1)

    res = [0] * (n + 1)
    for u in range(1, n + 1):
        res[u] = max(dp_inc[u], dp_dec[u])

    print(' '.join(map(str, res[1:])))

if __name__ == "__main__":
    main()
