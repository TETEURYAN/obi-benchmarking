import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n, m = data[0], data[1]
a = data[2:2 + n]

diff = [x - m for x in a]

moves = 0
carry = 0
for i in range(n - 1):
    x = diff[i] + carry
    moves += abs(x)
    carry = x

print(moves)