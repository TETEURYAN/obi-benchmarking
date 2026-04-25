import sys

data = sys.stdin.read().split()
N = int(data[0])
K = int(data[1])
primes = [int(x) for x in data[2:2+K]]

def inclusion(index, prod, sign):
    if index == K:
        return sign * (N // prod) if prod > 1 else 0
    res = inclusion(index + 1, prod, sign)
    if prod <= N // primes[index]:
        new_prod = prod * primes[index]
        res += inclusion(index + 1, new_prod, -sign)
    return res

div_by_at_least_one = inclusion(0, 1, 1)
answer = N - div_by_at_least_one
print(answer)