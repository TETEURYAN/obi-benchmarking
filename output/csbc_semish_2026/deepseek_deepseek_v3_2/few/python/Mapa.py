import sys
sys.setrecursionlimit(200000)

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        adj[a].append((b, c))
        adj[b].append((a, c))

    total_pairs = n * (n - 1) // 2
    visited = [False] * (n + 1)

    def dfs(u):
        visited[u] = True
        size = 1
        for v, c in adj[u]:
            if not visited[v] and c == 0:
                sz = dfs(v)
                size += sz
        return size

    blue_only_pairs = 0
    for i in range(1, n + 1):
        if not visited[i]:
            comp_size = dfs(i)
            blue_only_pairs += comp_size * (comp_size - 1) // 2

    result = total_pairs - blue_only_pairs
    print(result)

if __name__ == "__main__":
    solve()