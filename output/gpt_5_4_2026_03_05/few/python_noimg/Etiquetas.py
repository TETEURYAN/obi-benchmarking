import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n, k, c = data[0], data[1], data[2]
a = data[3:3+n]

total = sum(a)

pref = [0] * (n + 1)
for i in range(n):
    pref[i + 1] = pref[i] + a[i]

m = n - c + 1
w = [0] * (m + 1)
for i in range(1, m + 1):
    w[i] = pref[i + c - 1] - pref[i - 1]

neg_inf = -10**18
dp_prev = [0] * (m + 1)

for t in range(1, k + 1):
    dp_cur = [neg_inf] * (m + 1)
    best = neg_inf
    for i in range(1, m + 1):
        j = i - c
        if j >= 0:
            val = dp_prev[j]
            if val > best:
                best = val
        if best != neg_inf:
            dp_cur[i] = best + w[i]
        if dp_cur[i - 1] > dp_cur[i]:
            dp_cur[i] = dp_cur[i - 1]
    dp_prev = dp_cur

min_covered = dp_prev[m]
print(total - min_covered)