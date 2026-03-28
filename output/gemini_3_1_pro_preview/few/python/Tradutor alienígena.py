import sys

sys.setrecursionlimit(200000)

input_data = sys.stdin.read().split()
if not input_data:
    exit()

N_str = input_data[0]
S = input_data[1]

L = len(S)
len_N = len(N_str)

MOD = 1000000007

dp = [0] * (L + 1)
dp[0] = 1

W = 0

for i in range(1, L + 1):
    if S[i-1] != '0':
        W = (W + dp[i-1]) % MOD
        
    if i - len_N >= 0:
        if S[i - len_N] != '0':
            W = (W - dp[i - len_N] + MOD) % MOD
            
    dp[i] = W
    
    if i - len_N >= 0:
        if S[i - len_N] != '0':
            if S[i - len_N : i] <= N_str:
                dp[i] = (dp[i] + dp[i - len_N]) % MOD

print(dp[L])