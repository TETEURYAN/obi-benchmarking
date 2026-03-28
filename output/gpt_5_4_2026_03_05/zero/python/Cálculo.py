import sys

data = list(map(int, sys.stdin.read().split()))
m, n = data[0], data[1]
x = data[2:2 + m]
y = data[2 + m:2 + m + n]

i = m - 1
j = n - 1
carry = 0
res = []

while i >= 0 or j >= 0:
    s = carry
    if i >= 0:
        s += x[i]
        i -= 1
    if j >= 0:
        s += y[j]
        j -= 1
    res.append(s & 1)
    carry = s >> 1

while carry:
    res.append(carry & 1)
    carry >>= 1

while res and res[0] == 0:
    res.pop(0)

res.reverse()
print(' '.join(map(str, res)))