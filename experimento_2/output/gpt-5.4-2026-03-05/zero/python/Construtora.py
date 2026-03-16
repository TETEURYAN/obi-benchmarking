import sys

def solve(a):
    n = len(a)
    INF = 10**9
    dp = [[0]*n for _ in range(n)]
    for length in range(2, n+1):
        for l in range(n - length + 1):
            r = l + length - 1
            best = INF
            for k in range(l, r):
                v = dp[l][k] + dp[k+1][r]
                if v < best:
                    best = v
            if a[l] == a[r]:
                if length == 2:
                    best = min(best, 1)
                else:
                    best = min(best, dp[l+1][r-1] + 1)
            dp[l][r] = best
    return dp[0][n-1]

def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    a = data[1:1+n]
    print(solve(a))

if __name__ == "__main__":
    main()