
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:]))

if N == 0:
    print(0)
    sys.exit()

max_ap = 0
for i in range(N):
    if A[i] > 0:
        max_ap = max(max_ap, 1)

if max_ap == 0:
    print(0)
    sys.exit()

ans = 1
for d in range(1, N):
    cnt = {}
    for j in range(d, N):
        i = j - d
        if A[i] == 0 or A[j] == 0:
            continue
        k = min(A[i], A[j] - d)
        if k > 0:
            if k not in cnt:
                cnt[k] = 0
            cnt[k] += 1
    if cnt:
        ans = max(ans, max(cnt.values()) + 1)

print(ans)
