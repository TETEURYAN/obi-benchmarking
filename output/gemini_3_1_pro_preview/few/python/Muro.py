import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
MOD = 10**9 + 7

if n == 0:
    print(1)
elif n == 1:
    print(1)
elif n == 2:
    print(5)
else:
    a, b, c = 1, 1, 5
    for _ in range(3, n + 1):
        a, b, c = b, c, (c + 4 * b + 2 * a) % MOD
    print(c)