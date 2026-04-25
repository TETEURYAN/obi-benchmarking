import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])
m = int(data[1])

adj = [0] * n
idx = 2
for _ in range(m):
    x = int(data[idx]) - 1
    y = int(data[idx + 1]) - 1
    adj[x] |= 1 << y
    adj[y] |= 1 << x
    idx += 2

n1 = n // 2
n2 = n - n1

adj1 = [0] * n1
adj2 = [0] * n2
cross2 = [0] * n2

for i in range(n1):
    mask = adj[i]
    adj1[i] = mask & ((1 << n1) - 1)

for j in range(n2):
    mask = adj[n1 + j]
    adj2[j] = (mask >> n1) & ((1 << n2) - 1)
    cross2[j] = mask & ((1 << n1) - 1)

size1 = 1 << n1
ind1 = [False] * size1
ind1[0] = True
for mask in range(1, size1):
    b = mask & -mask
    v = b.bit_length() - 1
    prev = mask ^ b
    ind1[mask] = ind1[prev] and ((adj1[v] & prev) == 0)

dp = [0] * size1
for mask in range(size1):
    if ind1[mask]:
        dp[mask] = 1

for i in range(n1):
    bit = 1 << i
    for mask in range(size1):
        if mask & bit == 0 and dp[mask | bit] > dp[mask]:
            dp[mask] = dp[mask | bit]

size2 = 1 << n2
ind2 = [False] * size2
ind2[0] = True
ans = 0

for mask in range(size2):
    if mask:
        b = mask & -mask
        v = b.bit_length() - 1
        prev = mask ^ b
        ind2[mask] = ind2[prev] and ((adj2[v] & prev) == 0)
    if ind2[mask]:
        forbidden1 = 0
        mm = mask
        while mm:
            b = mm & -mm
            v = b.bit_length() - 1
            forbidden1 |= cross2[v]
            mm ^= b
        allowed1 = ((1 << n1) - 1) ^ forbidden1
        ans += dp[allowed1]

print(ans - 1)