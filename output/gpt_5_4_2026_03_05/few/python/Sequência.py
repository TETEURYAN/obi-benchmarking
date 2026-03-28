import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n, L, H = data[0], data[1], data[2]
s = data[3:3 + n]
m = data[3 + n:3 + 2 * n]

pref_sum = [0] * (n + 1)
pref_mark = [0] * (n + 1)

for i in range(1, n + 1):
    pref_sum[i] = pref_sum[i - 1] + s[i - 1]
    pref_mark[i] = pref_mark[i - 1] + m[i - 1]

total_marks = pref_mark[n]
best_min = [10**18] * (total_marks + 1)

ans = -10**18

for j in range(n + 1):
    cj = pref_mark[j]
    sj = pref_sum[j]

    low = cj - H
    if low < 0:
        low = 0
    high = cj - L
    if high >= 0:
        for c in range(low, high + 1):
            val = best_min[c]
            if val != 10**18:
                cur = sj - val
                if cur > ans:
                    ans = cur

    if sj < best_min[cj]:
        best_min[cj] = sj

print(ans)