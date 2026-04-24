import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])
h = list(map(int, data[1:1 + n]))

left = [0] * n
right = [0] * n

mx = 0
for i in range(n):
    if h[i] > mx:
        mx = h[i]
    left[i] = mx

mx = 0
for i in range(n - 1, -1, -1):
    if h[i] > mx:
        mx = h[i]
    right[i] = mx

ans = 0
for i in range(n):
    if min(left[i], right[i]) >= h[i] + 1:
        ans += 1

print(ans)