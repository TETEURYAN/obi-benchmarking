import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    N = int(data[0])
    dp = [0] * (N + 1)
    for x in range(1, N + 1):
        s = str(x)
        best = 10**9
        for ch in s:
            d = int(ch)
            if d > 0:
                if dp[x - d] < best:
                    best = dp[x - d]
        dp[x] = best + 1
    print(dp[N])

if __name__ == "__main__":
    main()