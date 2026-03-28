import sys

MOD = 10**9 + 7

def main():
    data = sys.stdin.read().split()
    if not data:
        print(1)
        return
    N = int(data[0])
    if N == 0:
        print(1)
        return
    if N == 1:
        print(1)
        return

    dp = [0] * (N + 1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 5

    for i in range(3, N + 1):
        dp[i] = (dp[i-1] + 4 * dp[i-2] + 2 * dp[i-3]) % MOD

    print(dp[N])

if __name__ == "__main__":
    main()