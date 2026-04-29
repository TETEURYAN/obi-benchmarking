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

    pref = [0] * (N + 1)
    for i in range(N):
        pref[i + 1] = pref[i] + a[i]

    # dp[i] = menor custo para processar prefixo de tamanho i
    # transições:
    # - manter último elemento: dp[i] = dp[i-1] + a[i-1]
    # - fundir últimos K elementos em um: dp[i] = dp[i-K] + OR(a[i-K..i-1])
    INF = 10**30
    dp = [INF] * (N + 1)
    dp[0] = 0

    # Para cada bit, manter quantidade no intervalo deslizante de tamanho K
    cnt = [0] * 30
    cur_or = 0

    for i in range(1, N + 1):
        x = a[i - 1]
        for b in range(30):
            if (x >> b) & 1:
                cnt[b] += 1
                cur_or |= (1 << b)

        if i > K:
            y = a[i - K - 1]
            for b in range(30):
                if (y >> b) & 1:
                    cnt[b] -= 1
                    if cnt[b] == 0:
                        cur_or &= ~(1 << b)

        dp[i] = dp[i - 1] + x
        if i >= K:
            v = dp[i - K] + cur_or
            if v < dp[i]:
                dp[i] = v

    print(dp[N])

if __name__ == "__main__":
    main()
