import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n, k = data[0], data[1]
a = data[2:2 + n]

freq = {0: 1}
s = 0
ans = 0

for x in a:
    s += x
    ans += freq.get(s - k, 0)
    freq[s] = freq.get(s, 0) + 1

print(ans)