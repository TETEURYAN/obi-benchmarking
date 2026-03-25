import sys

MOD = 1000000007

data = sys.stdin.read().split()
if not data:
    sys.exit()

N = data[0].strip()
S = data[1].strip()

L = len(N)
m = len(S)

if N == "0":
    print(0)
    sys.exit()

pow10 = [1] * (L + 1)
for i in range(1, L + 1):
    pow10[i] = pow10[i - 1] * 10

N_int = int(N)

def lcp_array(s, t):
    a = s + '#' + t
    n = len(a)
    z = [0] * n
    l = r = 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and a[z[i]] == a[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
    base = len(s) + 1
    res = [0] * len(t)
    for i in range(len(t)):
        v = z[base + i]
        if v > len(s):
            v = len(s)
        res[i] = v
    return res

lcp = lcp_array(N, S)

def leq_N(pos):
    common = lcp[pos]
    if common >= L:
        return True
    return S[pos + common] <= N[common]

dp = [0] * (m + 1)
pref = [0] * (m + 2)
dp[0] = 1
pref[1] = 1

for i in range(1, m + 1):
    if S[i - 1] != '0':
        if i < L:
            dp[i] = pref[i] % MOD
        else:
            left = i - L + 1
            val = (pref[i] - pref[left]) % MOD
            if leq_N(i - L):
                val += dp[i - L]
            dp[i] = val % MOD
    pref[i + 1] = (pref[i] + dp[i]) % MOD

print(dp[m] % MOD)