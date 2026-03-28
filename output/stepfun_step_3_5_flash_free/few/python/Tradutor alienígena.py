import sys

MOD = 1000000007

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    N_str = data[0]
    S = data[1] if len(data) > 1 else ''
    d = len(N_str)
    L = len(S)
    dp = [0] * (L + 1)
    dp[L] = 1
    for i in range(L - 1, -1, -1):
        if S[i] == '0':
            dp[i] = 0
        else:
            total = 0
            max_j = min(i + d + 1, L + 1)
            for j in range(i + 1, max_j):
                k = j - i
                if k < d:
                    total = (total + dp[j]) % MOD
                else:  # k == d
                    if S[i:j] <= N_str:
                        total = (total + dp[j]) % MOD
            dp[i] = total
    print(dp[0] % MOD)

if __name__ == "__main__":
    main()