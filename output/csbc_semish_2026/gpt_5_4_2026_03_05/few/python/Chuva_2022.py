import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
s = data[1]
a = data[2:2 + n]

ans = 0
left = 0
curr = 0

for right in range(n):
    curr += a[right]
    while left <= right and curr > s:
        curr -= a[left]
        left += 1

    if curr == s:
        if s == 0:
            ans += right - left + 1
        else:
            ans += 1
            t = left
            while t < right and a[t] == 0:
                ans += 1
                t += 1

print(ans)