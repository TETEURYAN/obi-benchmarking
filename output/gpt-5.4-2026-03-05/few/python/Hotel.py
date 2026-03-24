import sys

data = sys.stdin.read().split()
if not data:
    exit()

D = int(data[0])
A = int(data[1])
N = int(data[2])

daily = D + min(N - 1, 14) * A
days = 32 - N
print(daily * days)