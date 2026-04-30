
import sys

A = int(sys.stdin.readline().strip())
B = int(sys.stdin.readline().strip())

sa = str(A)
sb = str(B)

if len(sa) > len(sb):
    sb = '0' * (len(sa) - len(sb)) + sb
elif len(sb) > len(sa):
    sa = '0' * (len(sb) - len(sa)) + sa

la = list(sa)
lb = list(sb)

i = len(la) - 1
while i >= 0:
    da = int(la[i])
    db = int(lb[i])
    if da < db:
        lb[i] = ''
    elif db < da:
        la[i] = ''
    i -= 1

ra = ''.join(la).lstrip('0')
rb = ''.join(lb).lstrip('0')

if not ra:
    na = -1
else:
    na = int(ra)
if not rb:
    nb = -1
else:
    nb = int(rb)

if na == -1 and nb == -1:
    print(-1, -1)
elif na == -1:
    print(-1, nb)
elif nb == -1:
    print(-1, na)
elif na <= nb:
    print(na, nb)
else:
    print(nb, na)
