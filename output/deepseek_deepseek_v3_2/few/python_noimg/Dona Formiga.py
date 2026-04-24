import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
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
    
    dp = [-1] * (S + 1)
    
    def dfs(u: int) -> int:
        if dp[u] != -1:
            return dp[u]
        best = 0
        for v in adj[u]:
            best = max(best, dfs(v) + 1)
        dp[u] = best
        return best
    
    result = dfs(P)
    print(result)

if __name__ == "__main__":
    solve()