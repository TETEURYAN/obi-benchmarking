import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

m = int(input_data[0])
n = int(input_data[1])

x = [int(v) for v in input_data[2:2+m]]
y = [int(v) for v in input_data[2+m:2+m+n]]

L = max(m, n)
x.extend([0] * (L - m))
y.extend([0] * (L - n))

res = [0] * L
carry = 0
for i in range(L - 1, -1, -1):
    s = x[i] + y[i] + carry
    res[i] = s % 2
    carry = s // 2

while res and res[-1] == 0:
    res.pop()

print(*(res))