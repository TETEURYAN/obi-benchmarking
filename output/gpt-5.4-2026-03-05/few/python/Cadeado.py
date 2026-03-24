import sys

data = sys.stdin.read().split()
if not data:
    exit()

n = int(data[0])
ans = 0
idx = 1

for _ in range(n):
    c = int(data[idx])
    s = int(data[idx + 1])
    idx += 2
    d = abs(c - s)
    ans += min(d, 10 - d)

print(ans)