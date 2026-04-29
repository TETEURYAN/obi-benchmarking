import sys

MOD = 10**9 + 7

n = int(sys.stdin.readline())

if n == 0:
    print(1)
elif n == 1:
    print(1)
elif n == 2:
    print(5)
else:
    a0, a1, a2 = 1, 1, 5
    for i in range(3, n + 1):
        a0, a1, a2 = a1, a2, (2 * a2 + a0) % MOD
    print(a2)