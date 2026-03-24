import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

A = data[0]
B = data[1]

n = max(len(A), len(B))
A = A.zfill(n)
B = B.zfill(n)

ra = []
rb = []

for i in range(n - 1, -1, -1):
    da = A[i]
    db = B[i]
    if da > db:
        ra.append(da)
    elif db > da:
        rb.append(db)
    else:
        ra.append(da)
        rb.append(db)

sa = ''.join(reversed(ra))
sb = ''.join(reversed(rb))

va = -1 if sa == '' else int(sa)
vb = -1 if sb == '' else int(sb)

if va <= vb:
    print(va, vb)
else:
    print(vb, va)