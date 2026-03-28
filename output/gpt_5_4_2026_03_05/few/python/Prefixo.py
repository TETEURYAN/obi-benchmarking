import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])
p = data[1]
m = int(data[2])
s = data[3]

limit = min(n, m, len(p), len(s))
ans = 0
while ans < limit and p[ans] == s[ans]:
    ans += 1

print(ans)