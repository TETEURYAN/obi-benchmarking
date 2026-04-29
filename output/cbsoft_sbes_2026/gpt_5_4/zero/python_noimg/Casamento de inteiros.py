a = input().strip()
b = input().strip()

n = max(len(a), len(b))
a = a.zfill(n)
b = b.zfill(n)

ra = []
rb = []

for da, db in zip(a, b):
    if da > db:
        ra.append(da)
    elif db > da:
        rb.append(db)
    else:
        ra.append(da)
        rb.append(db)

sa = ''.join(ra)
sb = ''.join(rb)

va = -1 if sa == '' else int(sa)
vb = -1 if sb == '' else int(sb)

if va <= vb:
    print(va, vb)
else:
    print(vb, va)