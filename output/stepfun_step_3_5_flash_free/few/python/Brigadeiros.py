import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it)); K = int(next(it)); T = int(next(it))
    P = [int(next(it)) for _ in range(N)]
    G = [int(next(it)) for _ in range(N)]
    
    A = [i+1 for i in range(N) if G[i] == 1]
    A.sort()
    K = len(A)
    
    if K == 0:
        print(0)
        return
    
    max_valor = 9 * K
    INF = 10**9
    
    dp = [[INF] * (max_valor + 1) for _ in range(K+1)]
    dp[0][0] = 0
    
    for j in range(1, N+1):
        max_i = min(K-1, j-1)
        for i in range(max_i, -1, -1):
            max_v = 9 * i
            for v in range(0, max_v+1):
                if dp[i][v] == INF:
                    continue
                custo = dp[i][v] + abs(A[i] - j)
                if custo > T:
                    continue
                nv = v + P[j-1]
                if nv > max_valor:
                    continue
                if custo < dp[i+1][nv]:
                    dp[i+1][nv] = custo
    
    ans = 0
    for v in range(max_valor, -1, -1):
        if dp[K][v] <= T:
            ans = v
            break
    print(ans)

if __name__ == "__main__":
    main()