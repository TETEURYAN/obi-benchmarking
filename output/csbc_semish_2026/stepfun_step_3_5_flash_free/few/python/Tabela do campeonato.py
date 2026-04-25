import sys

data = sys.stdin.read().split()
if not data:
    exit()
j, p, v, e, d = map(int, data)

neg = [j == -1, p == -1, v == -1, e == -1, d == -1]
count = sum(neg)

if count == 1:
    if j == -1:
        j = v + e + d
    elif p == -1:
        p = 3 * v + e
    elif v == -1:
        v = (p - e) // 3
    elif e == -1:
        e = p - 3 * v
    else:
        d = j - v - e
elif count == 2:
    if j == -1 and p == -1:
        j = v + e + d
        p = 3 * v + e
    elif j == -1 and v == -1:
        v = (p - e) // 3
        j = v + e + d
    elif j == -1 and e == -1:
        e = p - 3 * v
        j = v + e + d
    elif p == -1 and v == -1:
        v = j - e - d
        p = 3 * v + e
    elif p == -1 and e == -1:
        e = j - v - d
        p = 3 * v + e
    elif p == -1 and d == -1:
        d = j - v - e
        p = 3 * v + e
    elif v == -1 and e == -1:
        v = (p - j + d) // 2
        e = j - d - v
    elif v == -1 and d == -1:
        v = (p - e) // 3
        d = j - v - e
    elif e == -1 and d == -1:
        e = p - 3 * v
        d = j - v - e

print(j, p, v, e, d)