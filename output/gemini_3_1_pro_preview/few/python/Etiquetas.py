import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

N = int(input_data[0])
K = int(input_data[1])
C = int(input_data[2])

A = [int(x) for x in input_data[3:]]

if K * C == N:
    print(0)
    exit()

if C == 1:
    A.sort()
    min_covered = sum(A[:K])
    print(sum(A) - min_covered)
    exit()

cost = [0] * (N + 1)
curr_sum = sum(A[:C])
cost[C] = curr_sum
for i in range(C + 1, N + 1):
    curr_sum += A[i - 1] - A[i - 1 - C]
    cost[i] = curr_sum

dp = [0] * (N + 1)
INF = 10**15

for j in range(1, K + 1):
    new_dp = [INF] * (N + 1)
    min_val = INF
    
    start_i = j * C
    end_i = N - (K - j) * C + 1
    
    dp_prev = dp[start_i - C : end_i - C]
    cost_curr = cost[start_i : end_i]
    
    idx = start_i
    for p, c in zip(dp_prev, cost_curr):
        if p < min_val:
            min_val = p
        new_dp[idx] = min_val + c
        idx += 1
        
    dp = new_dp

ans = sum(A) - min(dp[K * C : N + 1])
print(ans)