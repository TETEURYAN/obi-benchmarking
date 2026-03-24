import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
A = [int(x) for x in input_data[1:n+1]]

A.sort()

ans = 0
for i in range(n - 2):
    k = i + 2
    for j in range(i + 1, n - 1):
        while k < n and A[i] + A[j] > A[k]:
            k += 1
        ans += k - j - 1

print(ans)