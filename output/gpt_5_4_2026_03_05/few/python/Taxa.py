import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])
f_str = data[1]
x = list(map(int, data[2:2 + n]))

if n == 1:
    print("0.00")
    sys.exit()

if '.' in f_str:
    a, b = f_str.split('.')
    b = (b + '00')[:2]
    f100 = int(a) * 100 + int(b)
else:
    f100 = int(f_str) * 100

arr = x + x
m = 2 * n

pref = [0] * (m + 1)
for i in range(m):
    pref[i + 1] = pref[i] + arr[i]

INF = 10**30
dp = [[0] * m for _ in range(m)]

for length in range(2, n + 1):
    for l in range(0, m - length + 1):
        r = l + length - 1
        total = pref[r + 1] - pref[l]
        best = INF
        for k in range(l, r):
            left = pref[k + 1] - pref[l]
            right = total - left
            cost = dp[l][k] + dp[k + 1][r] + (left if left > right else right)
            if cost < best:
                best = cost
        dp[l][r] = best

ans = INF
for s in range(n):
    val = dp[s][s + n - 1]
    if val < ans:
        ans = val

result100 = ans * f100
print(f"{result100 // 100}.{result100 % 100:02d}")