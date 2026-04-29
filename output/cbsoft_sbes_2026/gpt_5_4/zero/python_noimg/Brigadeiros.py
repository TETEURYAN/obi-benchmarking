import sys

def main():
    input = sys.stdin.readline
    N, K, T = map(int, input().split())
    P = list(map(int, input().split()))
    G = list(map(int, input().split()))

    friends = [i + 1 for i, x in enumerate(G) if x == 1]  # 1-indexed positions

    NEG = -10**18

    # dp[j][s] = max sum using first processed positions,
    # having placed j friends, with total movement cost exactly s
    # We only need costs up to min(T, max_possible_cost)
    max_possible_cost = 0
    for i in range(K):
        max_possible_cost += abs((N - K + 1 + i) - friends[i])
    S = min(T, max_possible_cost)

    dp = [[NEG] * (S + 1) for _ in range(K + 1)]
    dp[0][0] = 0

    for pos in range(1, N + 1):
        val = P[pos - 1]
        upper_j = min(pos, K)
        for j in range(upper_j, 0, -1):
            cost = abs(pos - friends[j - 1])
            if cost > S:
                continue
            prev = dp[j - 1]
            cur = dp[j]
            for s in range(S, cost - 1, -1):
                cand = prev[s - cost] + val
                if cand > cur[s]:
                    cur[s] = cand

    ans = max(dp[K][:S + 1])
    print(ans)

if __name__ == "__main__":
    main()
