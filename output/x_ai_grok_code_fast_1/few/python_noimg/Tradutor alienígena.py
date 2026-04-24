import sys

MOD = 1000000007

N_str = input().strip()
S = input().strip()
L = len(S)
len_N = len(N_str)

dp = [0] * (L + 1)
dp[0] = 1

for i in range(1, L + 1):
    max_k = min(i, len_N)
    for k in range(1, max_k + 1):
        substr = S[i - k:i]
        if substr[0] == '0' and k > 1:
            continue
        if k == 1 and substr == '0':
            continue
        # check if substr <= N_str
        if len(substr) < len_N or (len(substr) == len_N and substr <= N_str):
            dp[i] = (dp[i] + dp[i - k]) % MOD

print(dp[L])