import sys
sys.setrecursionlimit(300000)

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    plans = [(int(next(it)), int(next(it)), int(next(it))) for _ in range(M)]

    def has_cycle(k):
        adj = [[] for _ in range(N + 1)]
        indeg = [0] * (N + 1)
        for i in range(k):
            u, l, r = plans[i]
            for v in range(l, r + 1):
                adj[u].append(v)
                indeg[v] += 1

        from collections import deque
        q = deque([i for i in range(1, N + 1) if indeg[i] == 0])
        cnt = 0
        while q:
            u = q.popleft()
            cnt += 1
            for v in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        return cnt != N

    lo, hi = 1, M
    ans = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if has_cycle(mid):
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    print(ans)

if __name__ == "__main__":
    main()