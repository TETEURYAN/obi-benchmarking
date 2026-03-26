import sys

n = int(sys.stdin.read().strip())

# Check if n has a divisor d such that 2 <= d <= n//2
# i.e., n is not 1 and not prime (has a composite factorization with both factors >= 2)

if n < 4:
    print('N')
else:
    found = False
    i = 2
    while i * i <= n:
        if n % i == 0:
            found = True
            break
        i += 1
    print('S' if found else 'N')