import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])
left = [0] * 61
right = [0] * 61

idx = 1
for _ in range(n):
    m = int(data[idx])
    l = data[idx + 1]
    if l == 'E':
        left[m] += 1
    else:
        right[m] += 1
    idx += 2

ans = 0
for size in range(30, 61):
    ans += min(left[size], right[size])

print(ans)