import sys

sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        S = int(next(iterator))
        T = int(next(iterator))
        P = int(next(iterator))
    except StopIteration:
        return

    heights = [0] * (S + 1)
    for i in range(1, S + 1):
        heights[i] = int(next(iterator))

    adj = [[] for _ in range(S + 1)]
    
    for _ in range(T):
        u = int(next(iterator))
        v = int(next(iterator))
        
        if heights[u] > heights[v]:
            adj[u].append(v)
        elif heights[v] > heights[u]:
            adj[v].append(u)
            
    dp = [-1] * (S + 1)

    def dfs(u):
        if dp[u] != -1:
            return dp[u]
        
        max_dist = 0
        for v in adj[u]:
            dist = 1 + dfs(v)
            if dist > max_dist:
                max_dist = dist
        
        dp[u] = max_dist
        return dp[u]

    print(dfs(P))

if __name__ == "__main__":
    solve()