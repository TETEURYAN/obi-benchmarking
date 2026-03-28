import sys

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx])
idx += 1
D = int(input_data[idx])
idx += 1
W = int(input_data[idx])
idx += 1
p = [int(x) for x in input_data[idx:]]

prefix = [0] * (N + 1)
for i in range(N):
    prefix[i + 1] = prefix[i] + p[i]

def can(L):
    if L < D:
        return False
    start = (L - D) // 2
    for left in range(N - L + 1):
        sum_D = prefix[left + start + D] - prefix[left + start]
        total = prefix[left + L] - prefix[left]
        cost = total - sum_D
        if cost <= W:
            return True
    return False

low = D
high = N
ans = D
while low <= high:
    mid = (low + high) // 2
    if can(mid):
        ans = mid
        low = mid + 1
    else:
        high = mid - 1

print(ans)