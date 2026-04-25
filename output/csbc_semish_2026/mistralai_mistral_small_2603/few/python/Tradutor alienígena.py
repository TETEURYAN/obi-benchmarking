
import sys

MOD = 1000000007

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    N_str = data[0]
    s = data[1] if len(data) > 1 else ""

    N = int(N_str)
    n = len(s)

    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        if s[i-1] != '0':
            dp[i] = dp[i-1]
        if i >= 2:
            num = int(s[i-2:i])
            if 1 <= num <= N:
                dp[i] = (dp[i] + dp[i-2]) % MOD
        if i >= 3:
            num = int(s[i-3:i])
            if 1 <= num <= N:
                dp[i] = (dp[i] + dp[i-3]) % MOD

    print(dp[n] % MOD)

if __name__ == "__main__":
    main()
