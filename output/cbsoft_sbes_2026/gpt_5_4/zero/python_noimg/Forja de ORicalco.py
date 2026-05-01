import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    N, K = data[0], data[1]
    a = data[2:2+N]

    if K > N:
        print(sum(a))
        return

    # dp[i] = menor custo para processar prefixo de tamanho i
    # Transições:
    # - manter a[i-1] sozinho: dp[i] = dp[i-1] + a[i-1]
    # - fundir um bloco de tamanho K terminando em i: dp[i] = dp[i-K] + OR(bloco)
    #
    # Como OR por bits é independente e custo final é soma, para cada bit b:
    # contribuição = 2^b * mínimo número de grupos finais que contêm ao menos um elemento com bit b = 1.
    # Isso equivale ao mesmo DP acima aplicado ao vetor binário daquele bit,
    # onde custo de manter elemento = 1 se bit presente, senão 0,
    # e custo de fundir bloco K = 1 se existe algum 1 no bloco, senão 0.

    ans = 0
    for b in range(30):
        pref = [0] * (N + 1)
        mask = 1 << b
        for i in range(N):
            pref[i + 1] = pref[i] + ((a[i] >> b) & 1)

        dp = [0] * (N + 1)
        for i in range(1, N + 1):
            bit_i = (a[i - 1] >> b) & 1
            best = dp[i - 1] + bit_i
            if i >= K:
                has_one = 1 if pref[i] - pref[i - K] > 0 else 0
                v = dp[i - K] + has_one
                if v < best:
                    best = v
            dp[i] = best

        ans += dp[N] * mask

    print(ans)

if __name__ == "__main__":
    main()
