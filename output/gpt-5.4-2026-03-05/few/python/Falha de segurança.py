import sys

data = sys.stdin.read().split()
if not data:
    exit()

n = int(data[0])
passwords = data[1:1 + n]

freq = {}
for s in passwords:
    freq[s] = freq.get(s, 0) + 1

ans = 0

for s, c in freq.items():
    subs = set()
    L = len(s)
    for i in range(L):
        for j in range(i + 1, L + 1):
            subs.add(s[i:j])
    total = 0
    for t in subs:
        total += freq.get(t, 0)
    ans += c * (total - 1)

print(ans)