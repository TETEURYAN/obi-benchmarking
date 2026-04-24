
def main():
    S = input().strip()
    n = len(S)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if S[j] <= S[i]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
    print(max(dp) if n > 0 else 0)

if __name__ == "__main__":
    main()
