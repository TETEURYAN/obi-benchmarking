import sys
sys.setrecursionlimit(200000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        a = int(data[idx])
        b = int(data[idx+1])
        adj[a].append(b)
        adj[b].append(a)
        idx += 2

    # Ordenar as listas de adjacência para facilitar busca
    for i in range(1, n + 1):
        adj[i].sort()

    # dp[u][parity] = maior caminho começando em u com u na posição parity (0 = par, 1 = impar)
    dp = [[1, 1] for _ in range(n + 1)]
    visited = [[False, False] for _ in range(n + 1)]

    def dfs(u, parity):
        if visited[u][parity]:
            return dp[u][parity]
        visited[u][parity] = True

        if parity == 0:  # u é par no caminho -> próximo deve ser maior (ímpar)
            # Devemos ir para um vizinho v > u
            # Usar busca binária para encontrar o primeiro v > u
            lo = 0
            hi = len(adj[u]) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if adj[u][mid] <= u:
                    lo = mid + 1
                else:
                    hi = mid - 1
            # Todos de lo até o final são > u
            for v in adj[u][lo:]:
                dp[u][parity] = max(dp[u][parity], 1 + dfs(v, 1))
        else:  # u é ímpar no caminho -> próximo deve ser menor (par)
            # Devemos ir para um vizinho v < u
            # Usar busca binária para encontrar o último v < u
            lo = 0
            hi = len(adj[u]) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if adj[u][mid] >= u:
                    hi = mid - 1
                else:
                    lo = mid + 1
            # Todos de 0 até hi são < u
            for v in adj[u][0:hi+1]:
                dp[u][parity] = max(dp[u][parity], 1 + dfs(v, 0))

        return dp[u][parity]

    for i in range(1, n + 1):
        dfs(i, 0)
        dfs(i, 1)

    result = []
    for i in range(1, n + 1):
        # O caminho pode começar como par ou ímpar, pegar o máximo
        result.append(max(dp[i][0], dp[i][1]))

    print(*result)

if __name__ == "__main__":
    solve()