
import sys

MOD = 10**9 + 7

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    N = int(data[0])
    K = int(data[1])

    if K == 1:
        print(0)
        return

    dp = [0] * (N + 1)
    dp[0] = 1
    dp[1] = 2

    for i in range(2, N + 1):
        if i < K:
            dp[i] = (dp[i-1] * 2) % MOD
        else:
            dp[i] = (dp[i-1] * 2 - dp[i-K]) % MOD

    print(dp[N] % MOD)

if __name__ == "__main__":
    main()
