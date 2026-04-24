import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
a = data[1:1 + n]

events = {}

for i, h in enumerate(a):
    if i == 0 or a[i - 1] < h:
        events[h] = events.get(h, 0) + 1
    if i == n - 1 or a[i + 1] < h:
        events[h] = events.get(h, 0) - 1

active = 0
ans = 0
for h in sorted(events):
    active += events[h]
    if active > ans:
        ans = active

print(ans)