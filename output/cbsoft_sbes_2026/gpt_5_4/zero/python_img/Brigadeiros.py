import sys

def main():
    input = sys.stdin.readline
    N, K, T = map(int, input().split())
    P = list(map(int, input().split()))
    G = list(map(int, input().split()))

    friends = [i + 1 for i, x in enumerate(G) if x == 1]

    NEG = -10**18

    # dp[j][s] = melhor soma usando alguns primeiros pratos,
    # escolhendo j posições finais para os j primeiros amigos,
    # com custo total s
    dp = [[NEG] * (T + 1) for _ in range(K + 1)]
    dp[0][0] = 0

    for pos in range(1, N + 1):
        val = P[pos - 1]
        upper = min(K, pos)
        for j in range(upper, 0, -1):
            cost = abs(friends[j - 1] - pos)
            if cost > T:
                continue
            prev = dp[j - 1]
            cur = dp[j]
            for s in range(T, cost - 1, -1):
                cand = prev[s - cost] + val
                if cand > cur[s]:
                    cur[s] = cand

    ans = max(dp[K])
    print(ans)

if __name__ == "__main__":
    main()
