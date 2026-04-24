
import sys

def main():
    S = sys.stdin.readline().strip()
    n = len(S)
    if n == 0:
        print(0)
        return

    last = [0] * 26
    for i in range(n):
        c = ord(S[i]) - ord('A')
        last[c] = i

    dp = [1] * n
    max_len = 1
    for i in range(1, n):
        c = ord(S[i]) - ord('A')
        for j in range(c):
            if last[j] < i:
                if dp[last[j]] + 1 > dp[i]:
                    dp[i] = dp[last[j]] + 1
        if dp[i] > max_len:
            max_len = dp[i]

    print(max_len)

if __name__ == "__main__":
    main()
