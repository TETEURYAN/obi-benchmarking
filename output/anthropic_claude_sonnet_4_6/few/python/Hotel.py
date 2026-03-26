import sys

data = sys.stdin.read().split()
D = int(data[0])
A = int(data[1])
N = int(data[2])

days = 32 - N
increment = min(N - 1, 15)
daily = D + increment * A
total = days * daily

print(total)