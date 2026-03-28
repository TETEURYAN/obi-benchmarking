import sys

def solve():
    data = sys.stdin.read().strip()
    if not data:
        return
    N = int(data)

    # DP array: dp[x] = minimum moves to reach 0 from x
    dp = [0] * (N + 1)

    for i in range(1, N + 1):
        # Get all digits of i
        digits = set()
        num = i
        while num > 0:
            d = num % 10
            if d > 0:
                digits.add(d)
            num //= 10
        # Compute dp[i] = 1 + min(dp[i - d]) for all d in digits
        best = 10**9
        for d in digits:
            if i - d >= 0:
                best = min(best, dp[i - d])
        dp[i] = 1 + best

    print(dp[N])

if __name__ == "__main__":
    solve()