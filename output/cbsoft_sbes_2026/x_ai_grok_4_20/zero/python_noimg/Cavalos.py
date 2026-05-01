
import sys

input = sys.stdin.read
data = input().split()
m = int(data[0])
n = int(data[1])

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
        print(4)
    elif n == 4:
        print(6)
    else:
        print((n // 2) * 2 + (n % 2))
else:
    total = m * n
    print((total + 1) // 2)
