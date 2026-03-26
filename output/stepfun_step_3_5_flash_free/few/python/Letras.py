import sys

def main():
    s = sys.stdin.read().strip()
    dp = [0] * 26
    for c in s:
        x = ord(c) - 65
        best = 0
        for i in range(x + 1):
            if dp[i] > best:
                best = dp[i]
        dp[x] = best + 1
    print(max(dp))

if __name__ == "__main__":
    main()