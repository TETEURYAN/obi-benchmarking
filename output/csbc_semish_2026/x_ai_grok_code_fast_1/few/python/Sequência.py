import sys

data = sys.stdin.read().split()
N = int(data[0])
L = int(data[1])
H = int(data[2])
S = list(map(int, data[3:3+N]))
M = list(map(int, data[3+N:3+2*N]))

ans = 0 if L == 0 else float('-inf')

for K in range(L, H+1):
    min_prefix = {}
    min_prefix[0] = 0
    current_sum = 0
    current_count = 0
    for i in range(N):
        current_sum += S[i]
        current_count += M[i]
        target_count = current_count - K
        if target_count in min_prefix:
            candidate = current_sum - min_prefix[target_count]
            if candidate > ans:
                ans = candidate
        if current_count not in min_prefix:
            min_prefix[current_count] = current_sum
        else:
            min_prefix[current_count] = min(min_prefix[current_count], current_sum)

print(ans)