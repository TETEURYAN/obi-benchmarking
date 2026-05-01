import sys

MOD = 10**9 + 7

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    N = int(data[0])
    K = int(data[1])

    # dp[i][j] = número de sequências de i bits que terminam com exatamente j uns consecutivos
    dp = [[0] * K for _ in range(N + 1)]
    dp[0][0] = 1  # sequência vazia

    for i in range(1, N + 1):
        # colocar um 0 no final
        total = sum(dp[i - 1][j] for j in range(K)) % MOD
        dp[i][0] = total

        # colocar um 1 no final
        for j in range(1, K):
            dp[i][j] = dp[i - 1][j - 1]

    # resposta: soma de todas as sequências de N bits que não têm K uns consecutivos
    ans = sum(dp[N][j] for j in range(K)) % MOD
    print(ans)

if __name__ == "__main__":
    main()