import sys
sys.setrecursionlimit(300010)

def read_input():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx])
    K = int(data[idx + 1])
    idx += 2
    adj = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a = int(data[idx])
        b = int(data[idx + 1])
        adj[a].append(b)
        adj[b].append(a)
        idx += 2
    return N, K, adj

def dfs(u, p, R, adj, dp):
    children_cost = []
    for v in adj[u]:
        if v != p:
            dfs(v, u, R, adj, dp)
            if R >= 1:
                children_cost.append(dp[v][0])
            else:
                children_cost.append(dp[v][1])
    
    sum_cost = sum(children_cost) if children_cost else 0
    
    # dp[u][0]: u is covered by outside
    dp[u][0] = min(sum_cost, 1 + sum_cost)
    
    # dp[u][1]: u is not covered by outside, must place center at u or somewhere covering u
    dp[u][1] = 1 + sum_cost

def check(R, N, K, adj):
    dp = [[0, 0] for _ in range(N + 1)]
    dfs(1, -1, R, adj, dp)
    return dp[1][1] <= K

def solve(N, K, adj):
    left, right = 0, N - 1
    ans = right
    while left <= right:
        mid = (left + right) // 2
        if check(mid, N, K, adj):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans

N, K, adj = read_input()
print(solve(N, K, adj))