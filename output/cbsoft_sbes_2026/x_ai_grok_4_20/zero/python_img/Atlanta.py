
import sys
import math

A = int(sys.stdin.readline().strip())
B = int(sys.stdin.readline().strip())

if A % 4 != 0:
    print(-1, -1)
    sys.exit(0)

P = A // 4
D = int(math.sqrt(B))
found = False
ans_l = -1
ans_w = -1

for l in range(D, 0, -1):
    if B % l == 0:
        w = B // l
        if w > l:
            continue
        if (l - 2) * (w - 2) == B and l >= 3 and w >= 3:
            if (l + w - 2) * 2 == P:
                ans_l = w
                ans_w = l
                found = True
                break

if not found:
    for w in range(D, 0, -1):
        if B % w == 0:
            l = B // w
            if l < w:
                continue
            if (l - 2) * (w - 2) == B and l >= 3 and w >= 3:
                if (l + w - 2) * 2 == P:
                    ans_l = w
                    ans_w = l
                    found = True
                    break

if found:
    if ans_l > ans_w:
        ans_l, ans_w = ans_w, ans_l
    print(ans_l, ans_w)
else:
    print(-1, -1)
