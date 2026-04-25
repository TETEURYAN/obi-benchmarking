import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n, d, w = data[0], data[1], data[2]
p = data[3:3+n]

pref = [0] * (n + 1)
for i in range(n):
    pref[i + 1] = pref[i] + p[i]

m = n - d + 1
A = [0] * m
B = [0] * m

for s in range(m):
    A[s] = pref[s]
    B[s] = pref[s + d]

INF = 10**30

left = [0] * m
l = 0
for s in range(m):
    while l <= s and A[s] - A[l] > w:
        l += 1
    left[s] = l

right = [0] * m
r = m - 1
for s in range(m - 1, -1, -1):
    while r >= s and B[r] - B[s] > w:
        r -= 1
    right[s] = r

ans = d
for s in range(m):
    total = d + (s - left[s]) + (right[s] - s)
    if total > ans:
        ans = total

print(ans)