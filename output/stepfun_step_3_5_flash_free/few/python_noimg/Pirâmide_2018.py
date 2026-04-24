import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    A = []
    for _ in range(N):
        row = [int(next(it)) for _ in range(N)]
        A.append(row)
    
    prefix = []
    for i in range(N):
        pref = [0] * (N + 1)
        for j in range(1, N + 1):
            pref[j] = pref[j - 1] + A[i][j - 1]
        prefix.append(pref)
    
    INF = 10**18
    dp = [[INF] * (N + 2) for _ in range(N + 2)]
    dp[N][1] = prefix[N - 1][N]
    
    for i in range(N - 1, 0, -1):
        for j in range(1, N - i + 2):
            l = j - 1
            r = j + i - 2
            custo = prefix[i - 1][r + 1] - prefix[i - 1][l]
            opcoes = []
            if j <= N - i:
                opcoes.append(dp[i + 1][j])
            if j - 1 >= 1 and j - 1 <= N - i:
                opcoes.append(dp[i + 1][j - 1])
            dp[i][j] = custo + min(opcoes)
    
    ans = min(dp[1][j] for j in range(1, N + 1))
    print(ans)

if __name__ == "__main__":
    main()