import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
A = list(map(int, input_data[1:]))
A.sort()
count = 0
for k in range(2, N):
    left = 0
    right = k - 1
    while left < right:
        if A[left] + A[right] > A[k]:
            count += (right - left)
            right -= 1
        else:
            left += 1
print(count)