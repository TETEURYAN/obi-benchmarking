import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

m = int(data[0])
n = int(data[1])

x = list(map(int, data[2:2 + m]))
y = list(map(int, data[2 + m:2 + m + n]))

L = max(m, n)
a = [0] * L
b = [0] * L

a[:m] = x
b[:n] = y

res = [0] * (L + 1)
carry = 0

for i in range(L - 1, -1, -1):
    s = a[i] + b[i] + carry
    res[i + 1] = s & 1
    carry = s >> 1

res[0] = carry

while len(res) > 1 and res[-1] == 0:
    res.pop()

print(*res)