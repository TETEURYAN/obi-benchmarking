import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

N = int(input_data[0])
D = int(input_data[1])

C = [int(x) for x in input_data[2:2+N]]

ans = 0

current_sum = 0
left = 0
for right in range(N):
    current_sum += C[right]
    while current_sum > D and left <= right:
        current_sum -= C[left]
        left += 1
    if current_sum == D:
        ans += 1

S = sum(C)
if S == D:
    ans += N - 1
elif S > D:
    target = S - D
    current_sum = 0
    left = 1
    for right in range(1, N - 1):
        current_sum += C[right]
        while current_sum > target and left <= right:
            current_sum -= C[left]
            left += 1
        if current_sum == target:
            ans += 1

print(ans)