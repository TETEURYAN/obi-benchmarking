import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
A = [int(x) for x in input_data[1:]]

left = 0
max_len = 0
seen = set()

for right in range(N):
    while A[right] in seen:
        seen.remove(A[left])
        left += 1
    seen.add(A[right])
    max_len = max(max_len, right - left + 1)

print(max_len)