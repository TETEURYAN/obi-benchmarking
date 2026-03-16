import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    n = data[0]
    a = data[1:1+n]

    INF = 10**9
    dp = [[0]*n for _ in range(n)]

    for length in range(2, n+1):
        for l in range(n - length + 1):
            r = l + length - 1
            best = INF
            for k in range(l, r):
                val = dp[l][k] + dp[k+1][r]
                if a[l] == a[k+1]:
                    val -= 1
                if val < best:
                    best = val
            dp[l][r] = best

    print(dp[0][n-1])

if __name__ == "__main__":
    main()
