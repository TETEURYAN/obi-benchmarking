
import sys

def longest_palindrome(s):
    n = len(s)
    if n == 0:
        return 0
    dp = [[False] * n for _ in range(n)]
    max_len = 1

    for i in range(n):
        dp[i][i] = True

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            max_len = 2

    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if length > max_len:
                    max_len = length
    return max_len

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    s = data[1] if len(data) > 1 else ""
    print(longest_palindrome(s))

if __name__ == "__main__":
    main()
