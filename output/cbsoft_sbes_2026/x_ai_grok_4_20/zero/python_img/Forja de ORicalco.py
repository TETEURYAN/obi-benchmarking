
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
K = int(data[1])
A = [int(x) for x in data[2:2+N]]

if K == 1:
    print(sum(A))
    sys.exit(0)

ans = 0
i = 0
while i < N:
    if i + K > N:
        ans += A[i]
        i += 1
        continue
    cur_or = 0
    for j in range(i, i + K):
        cur_or |= A[j]
    ans += cur_or
    i += K - 1

print(ans)
