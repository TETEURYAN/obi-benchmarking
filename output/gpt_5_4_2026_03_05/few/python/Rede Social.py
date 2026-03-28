import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])
r = list(map(int, data[1:1 + n]))
r.sort(reverse=True)

ans = 0
for i, x in enumerate(r, 1):
    if x >= i:
        ans = i
    else:
        break

print(ans)