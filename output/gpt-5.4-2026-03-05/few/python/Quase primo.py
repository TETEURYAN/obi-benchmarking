import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

N = data[0]
K = data[1]
primes = data[2:2 + K]
primes.sort()

ans = 0

def dfs(idx, prod, sign):
    global ans
    for i in range(idx, K):
        p = primes[i]
        if prod > N // p:
            break
        new_prod = prod * p
        ans += sign * (N // new_prod)
        dfs(i + 1, new_prod, -sign)

dfs(0, 1, 1)
print(N - ans)