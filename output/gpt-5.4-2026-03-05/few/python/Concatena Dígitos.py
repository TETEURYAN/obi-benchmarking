import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    exit()

n, q = data[0], data[1]
digits = data[2:2 + n]

prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + digits[i]

out = []
idx = 2 + n
for _ in range(q):
    l = data[idx]
    r = data[idx + 1]
    idx += 2

    length = r - l + 1
    if length < 2:
        out.append("0")
    else:
        s = prefix[r] - prefix[l - 1]
        out.append(str(11 * (length - 1) * s))

sys.stdout.write("\n".join(out))