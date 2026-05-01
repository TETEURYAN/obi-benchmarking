
MOD = 10**9 + 7

def main():
    N = int(input().strip())
    if N == 0:
        print(1)
        return
    if N == 1:
        print(1)
        return
    if N == 2:
        print(5)
        return

    dp = [0] * (N + 1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 5

    for i in range(3, N + 1):
        dp[i] = (dp[i-1] + 2 * dp[i-2] + 2 * dp[i-3]) % MOD

    print(dp[N] % MOD)

if __name__ == '__main__':
    main()
