import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    S = int(next(it))
    T = int(next(it))
    P = int(next(it))
    heights = [0] * (S + 1)
    for i in range(1, S + 1):
        heights[i] = int(next(it))
    adj = [[] for _ in range(S + 1)]
    for _ in range(T):
        u = int(next(it))
        v = int(next(it))
        if heights[u] > heights[v]:
            adj[u].append(v)
        elif heights[v] > heights[u]:
            adj[v].append(u)
    sys.setrecursionlimit(10000)
    dp = [-1] * (S + 1)
    def dfs(u):
        if dp[u] != -1:
            return dp[u]
        dp[u] = 1
        for v in adj[u]:
            dp[u] = max(dp[u], 1 + dfs(v))
        return dp[u]
    ans = dfs(P) - 1
    print(ans)

if __name__ == "__main__":
    main()