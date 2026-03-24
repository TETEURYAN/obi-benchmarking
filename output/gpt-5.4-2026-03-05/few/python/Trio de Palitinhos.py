import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
a = data[1:1+n]
a.sort()

ans = 0
for k in range(n - 1, 1, -1):
    i = 0
    j = k - 1
    ak = a[k]
    while i < j:
        if a[i] + a[j] > ak:
            ans += j - i
            j -= 1
        else:
            i += 1

print(ans)