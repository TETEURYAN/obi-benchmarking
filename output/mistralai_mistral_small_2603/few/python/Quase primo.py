
import sys
import math

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    k = int(data[1])
    primes = list(map(int, data[2:2+k]))

    def inclusion_exclusion(mask):
        product = 1
        sign = -1
        for i in range(k):
            if mask & (1 << i):
                if product > n // primes[i]:
                    return 0
                product *= primes[i]
                sign *= -1
        return sign * (n // product)

    total = 0
    for mask in range(1, 1 << k):
        total += inclusion_exclusion(mask)
    print(n - total)

if __name__ == "__main__":
    main()
