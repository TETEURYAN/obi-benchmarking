import sys
import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = math.isqrt(n)
    i = 3
    while i <= limit:
        if n % i == 0:
            return False
        i += 2
    return True

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    N = int(data[0])
    if N == 1:
        print('N')
    elif not is_prime(N):
        print('S')
    else:
        print('N')

if __name__ == '__main__':
    main()