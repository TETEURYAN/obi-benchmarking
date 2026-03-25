
import sys

data = sys.stdin.read().split()
if not data:
    exit()

N = int(data[0])
R = int(data[1])
P = int(data[2])

total = N
days = 0
infected = N

while total < P:
    infected *= R
    total += infected
    days += 1

print(days)
