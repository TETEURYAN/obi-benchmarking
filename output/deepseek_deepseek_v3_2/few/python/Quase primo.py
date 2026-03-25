import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    N = int(data[0])
    K = int(data[1])
    primes = list(map(int, data[2:2+K]))
    
    total = N
    # Princípio da Inclusão-Exclusão
    for mask in range(1, 1 << K):
        prod = 1
        bits = 0
        for i in range(K):
            if mask & (1 << i):
                bits += 1
                if prod > N // primes[i]:  # Evita overflow
                    prod = N + 1
                    break
                prod *= primes[i]
        if prod > N:
            continue
        if bits % 2 == 1:
            total -= N // prod
        else:
            total += N // prod
    
    print(total)

if __name__ == "__main__":
    main()