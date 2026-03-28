
import sys

def main():
    s = sys.stdin.readline().strip()
    dp = [0] * 26
    for c in s:
        idx = ord(c) - ord('A')
        best = max(dp[:idx + 1])
        dp[idx] = max(dp[idx], best + 1)
    print(max(dp))

if __name__ == "__main__":
    main()
