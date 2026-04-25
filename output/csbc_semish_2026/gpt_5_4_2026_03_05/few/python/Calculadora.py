import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])

exp = [0] * 10
idx = 1

for _ in range(n):
    d = int(data[idx])
    op = data[idx + 1]
    if op == '*':
        exp[d] += 1
    else:
        exp[d] -= 1
    idx += 2

primes = [2, 3, 5, 7]
fact = {
    1: (),
    2: (2,),
    3: (3,),
    4: (2, 2),
    5: (5,),
    6: (2, 3),
    7: (7,),
    8: (2, 2, 2),
    9: (3, 3),
}

pexp = {2: 0, 3: 0, 5: 0, 7: 0}

for d in range(2, 10):
    e = exp[d]
    if e:
        for p in fact[d]:
            pexp[p] += e

ans = 1
for p in primes:
    e = pexp[p]
    if e > 0:
        ans *= pow(p, e)

print(ans)