import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    N = int(data[0])
    F_str = data[1]
    X = list(map(int, data[2:2 + N]))

    # Converte F para centésimos para evitar erros de ponto flutuante
    if '.' in F_str:
        a, b = F_str.split('.')
        b = (b + '00')[:2]
    else:
        a, b = F_str, '00'
    F100 = int(a) * 100 + int(b)

    if N == 1 or F100 == 0:
        print("0.00")
        return

    # Duplica para tratar circularidade
    A = X + X
    M = 2 * N

    pref = [0] * (M + 1)
    for i in range(M):
        pref[i + 1] = pref[i] + A[i]

    def interval_sum(l, r):
        return pref[r + 1] - pref[l]

    INF = 10**30
    dp = [[0] * M for _ in range(M)]

    # dp[l][r] = custo mínimo (sem multiplicar por F) para dividir intervalo linear [l..r]
    # recorrência:
    # dp[l][r] = min_k dp[l][k] + dp[k+1][r] + max(sum(l..k), sum(k+1..r))
    for length in range(2, N + 1):
        for l in range(0, M - length + 1):
            r = l + length - 1
            best = INF
            total = interval_sum(l, r)
            for k in range(l, r):
                left = interval_sum(l, k)
                right = total - left
                cost = dp[l][k] + dp[k + 1][r] + (left if left > right else right)
                if cost < best:
                    best = cost
            dp[l][r] = best

    ans_base = INF
    for s in range(N):
        val = dp[s][s + N - 1]
        if val < ans_base:
            ans_base = val

    ans_cents = ans_base * F100
    print(f"{ans_cents // 100}.{ans_cents % 100:02d}")

if __name__ == "__main__":
    main()
