import sys

def parse_factor_to_cents(s):
    if '.' in s:
        a, b = s.split('.')
        b = (b + '00')[:2]
    else:
        a, b = s, '00'
    return int(a) * 100 + int(b)

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    N = int(data[0])
    F_cents = parse_factor_to_cents(data[1])
    X = list(map(int, data[2:2 + N]))

    if N == 1 or F_cents == 0:
        print("0.00")
        return

    A = X + X
    pref = [0] * (2 * N + 1)
    for i in range(2 * N):
        pref[i + 1] = pref[i] + A[i]

    INF = 10**18
    dp = [[0] * (2 * N) for _ in range(2 * N)]

    for length in range(2, N + 1):
        for l in range(0, 2 * N - length + 1):
            r = l + length - 1
            total = pref[r + 1] - pref[l]
            best = INF
            for k in range(l, r):
                left = pref[k + 1] - pref[l]
                right = total - left
                cost = dp[l][k] + dp[k + 1][r] + max(left, right)
                if cost < best:
                    best = cost
            dp[l][r] = best

    ans_units = INF
    for s in range(N):
        val = dp[s][s + N - 1]
        if val < ans_units:
            ans_units = val

    total_cents = ans_units * F_cents
    print(f"{total_cents // 100}.{total_cents % 100:02d}")

if __name__ == "__main__":
    main()
