import sys

data = sys.stdin.read().split()
N = int(data[0])
P = int(data[1])

days = 0
current = 1
while current * P <= N:
    current *= P
    days += 1

print(days)