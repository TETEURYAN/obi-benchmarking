import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    exit()

v, a, f, p = data
contas = sorted([a, f, p])

ans = 0
for x in contas:
    if v >= x:
        v -= x
        ans += 1
    else:
        break

print(ans)