
import sys

def main():
    m, n = map(int, sys.stdin.readline().split())
    if m > n:
        m, n = n, m
    if m == 1:
        print(n)
    elif m == 2:
        print((n // 4) * 4 + (4 if n % 4 == 1 or n % 4 == 2 else 2 if n % 4 == 3 else 0))
    elif m == 3:
        if n == 1:
            print(1)
        elif n == 2:
            print(4)
        elif n == 3:
            print(5)
        else:
            print((n // 2) * 2 + (n % 2))
    else:
        total = m * n
        print((total + 1) // 2)

if __name__ == "__main__":
    main()
