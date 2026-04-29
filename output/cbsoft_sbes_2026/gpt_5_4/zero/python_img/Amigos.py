import sys

def min_cost_to_targets(pos, targets):
    return sum(abs(p - t) for p, t in zip(pos, targets))

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    N, K = data[0], data[1]
    a = data[2:2 + N]
    b = data[2 + N:2 + 2 * N]

    top = [i + 1 for i, x in enumerate(a) if x == 1]
    bot = [i + 1 for i, x in enumerate(b) if x == 1]

    pref_top = [0] * (K + 1)
    pref_bot = [0] * (K + 1)
    for i in range(K):
        pref_top[i + 1] = pref_top[i] + top[i]
        pref_bot[i + 1] = pref_bot[i] + bot[i]

    ans = None

    for l in range(1, N - K + 2):
        r = l + K - 1

        sum_targets = K * l + K * (K - 1) // 2

        cost_top = pref_top[K] - sum_targets
        cost_bot = pref_bot[K] - sum_targets

        total = cost_top + cost_bot
        if ans is None or total < ans:
            ans = total

    print(ans)

if __name__ == "__main__":
    main()
