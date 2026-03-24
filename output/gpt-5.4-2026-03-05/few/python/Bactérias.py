import sys

data = sys.stdin.read().split()
if not data:
    exit()

n = int(data[0])
p = int(data[1])

days = 0
bacteria = 1

while bacteria <= n // p:
    bacteria *= p
    days += 1

print(days)