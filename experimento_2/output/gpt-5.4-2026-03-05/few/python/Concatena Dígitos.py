import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n, q = data[0], data[1]
d = data[2:2 + n]

pref = [0] * (n + 1)
for i in range(n):
    pref[i + 1] = pref[i] + d[i]

out = []
idx = 2 + n
for _ in range(q):
    l = data[idx]
    r = data[idx + 1]
    idx += 2

    s = pref[r] - pref[l - 1]
    k = r - l + 1
    if k <= 1:
        out.append("0")
    else:
        out.append(str(11 * (k - 1) * s))

sys.stdout.write("\n".join(out))