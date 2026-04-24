import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
v = data[1:1+n]

dp1 = 0
dp2 = 0

for x in v:
    if x == 1:
        new1 = max(dp1, dp2 + 1, 1)
        new2 = dp2
    else:
        new2 = max(dp2, dp1 + 1, 1)
        new1 = dp1
    dp1, dp2 = new1, new2

print(max(dp1, dp2))