import sys

data = list(map(int, sys.stdin.read().split()))
n = data[0]
a = data[1:1 + n]

soma = a[0] + a[-1]
ok = True

for i in range(n // 2):
    if a[i] + a[n - 1 - i] != soma:
        ok = False
        break

print('S' if ok else 'N')