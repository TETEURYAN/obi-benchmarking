import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    N, K = data[0], data[1]
    T = data[2:]
    T.sort()

    INF = 10**18

    # dp[j] = menor custo usando parte já processada e formando j trios
    dp = [INF] * (K + 1)
    dp[0] = 0

    # Processa da maior para a menor boneca.
    # Ao escolher um trio, usamos a boneca atual como a maior (C)
    # e as duas imediatamente anteriores como A e B.
    # C não influencia no custo, apenas garante A <= B <= C.
    for i in range(2, N):
        cost = (T[i - 1] - T[i - 2]) ** 2
        upper = min(K, (i + 1) // 3)
        for j in range(upper, 0, -1):
            cand = dp[j - 1] + cost
            if cand < dp[j]:
                dp[j] = cand

    print(dp[K])

if __name__ == "__main__":
    main()
