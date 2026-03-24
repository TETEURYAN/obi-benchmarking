import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

idx = 0
n = int(data[idx])
idx += 1

comp = [0] * (n + 1)
cid = 0

for i in range(1, n + 1):
    row = data[idx]
    idx += 1
    if comp[i] == 0:
        cid += 1
        comp[i] = cid
        for j, ch in enumerate(row, 1):
            if ch == '1':
                comp[j] = cid

e = int(data[idx])
idx += 1

out = []
for _ in range(e):
    k = int(data[idx])
    idx += 1
    seen = set()
    ans = 'N'
    for _ in range(k):
        c = int(data[idx])
        idx += 1
        cc = comp[c]
        if cc in seen:
            ans = 'S'
        else:
            seen.add(cc)
    out.append(ans)

sys.stdout.write('\n'.join(out))