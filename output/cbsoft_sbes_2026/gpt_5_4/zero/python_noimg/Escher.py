import sys

data = list(map(int, sys.stdin.read().split()))
n = data[0]
a = data[1:1+n]

soma = a[0] + a[-1]
i, j = 0, n - 1
ok = True

while i < j:
    if a[i] + a[j] != soma:
        ok = False
        break
    i += 1
    j -= 1

print('S' if ok else 'N')