import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n, I, F = data[0], data[1], data[2]
a = data[3:3+n]
a.sort()

def count_leq(x):
    l = 0
    r = n - 1
    cnt = 0
    while l < r:
        s = a[l] + a[r]
        if s <= x:
            cnt += r - l
            l += 1
        else:
            r -= 1
    return cnt

print(count_leq(F) - count_leq(I - 1))