import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
k = int(input_data[1])

U = []
C = []

current_sum = 0
U.append(0)
C.append(1)

for i in range(2, n + 2):
    val = int(input_data[i])
    if val == 0:
        C[-1] += 1
    else:
        current_sum += val
        U.append(current_sum)
        C.append(1)

ans = 0

if k == 0:
    for c in C:
        ans += c * (c - 1) // 2
else:
    left = 0
    right = 0
    m = len(U)
    while right < m:
        diff = U[right] - U[left]
        if diff == k:
            ans += C[left] * C[right]
            right += 1
            left += 1
        elif diff < k:
            right += 1
        else:
            left += 1

print(ans)