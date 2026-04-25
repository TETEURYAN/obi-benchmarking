import sys
import math

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

it = iter(data)
n = next(it)
m = next(it)
arr = [next(it) for _ in range(n)]

def is_good(x):
    return 1 if x > 1 else 0

b = [is_good(x) for x in arr]

size = 1
while size < n:
    size <<= 1

seg_len = [0] * (2 * size)
seg_pref = [0] * (2 * size)
seg_suf = [0] * (2 * size)
seg_ans = [0] * (2 * size)

for i in range(n):
    v = b[i]
    p = size + i
    seg_len[p] = 1
    seg_pref[p] = v
    seg_suf[p] = v
    seg_ans[p] = v

for p in range(size - 1, 0, -1):
    l = p << 1
    r = l | 1
    lenL = seg_len[l]
    lenR = seg_len[r]
    seg_len[p] = lenL + lenR
    seg_pref[p] = seg_pref[l] + (seg_pref[r] if seg_pref[l] == lenL else 0)
    seg_suf[p] = seg_suf[r] + (seg_suf[l] if seg_suf[r] == lenR else 0)
    seg_ans[p] = seg_ans[l] + seg_ans[r] + seg_suf[l] * seg_pref[r]

def update(pos, val):
    p = size + pos
    seg_len[p] = 1
    seg_pref[p] = val
    seg_suf[p] = val
    seg_ans[p] = val
    p >>= 1
    while p:
        l = p << 1
        r = l | 1
        lenL = seg_len[l]
        lenR = seg_len[r]
        seg_len[p] = lenL + lenR
        seg_pref[p] = seg_pref[l] + (seg_pref[r] if seg_pref[l] == lenL else 0)
        seg_suf[p] = seg_suf[r] + (seg_suf[l] if seg_suf[r] == lenR else 0)
        seg_ans[p] = seg_ans[l] + seg_ans[r] + seg_suf[l] * seg_pref[r]
        p >>= 1

def merge(a, b):
    if a[0] == 0:
        return b
    if b[0] == 0:
        return a
    lenA, prefA, sufA, ansA = a
    lenB, prefB, sufB, ansB = b
    total_len = lenA + lenB
    total_pref = prefA + (prefB if prefA == lenA else 0)
    total_suf = sufB + (sufA if sufB == lenB else 0)
    total_ans = ansA + ansB + sufA * prefB
    return (total_len, total_pref, total_suf, total_ans)

def query(l, r):
    l += size
    r += size
    left_res = (0, 0, 0, 0)
    right_res = (0, 0, 0, 0)
    while l <= r:
        if l & 1:
            left_res = merge(left_res, (seg_len[l], seg_pref[l], seg_suf[l], seg_ans[l]))
            l += 1
        if not (r & 1):
            right_res = merge((seg_len[r], seg_pref[r], seg_suf[r], seg_ans[r]), right_res)
            r -= 1
        l >>= 1
        r >>= 1
    res = merge(left_res, right_res)
    return res[3]

out = []
for _ in range(m):
    t = next(it)
    x = next(it)
    y = next(it)
    if t == 1:
        v = is_good(y)
        update(x - 1, v)
    else:
        out.append(str(query(x - 1, y - 1)))

sys.stdout.write("\n".join(out))