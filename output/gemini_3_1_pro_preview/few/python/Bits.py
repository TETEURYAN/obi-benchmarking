import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
k = int(input_data[1])

MOD = 10**9 + 7

S = [0] * (n + 1)
S[0] = 1
current_sum = 1

for i in range(1, n + 1):
    if i < k:
        S[i] = (current_sum + 1) % MOD
        current_sum = (current_sum + S[i]) % MOD
    else:
        S[i] = current_sum
        current_sum = (current_sum + S[i] - S[i - k]) % MOD

print(S[n])