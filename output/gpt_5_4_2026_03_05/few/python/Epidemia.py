import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

N = int(data[0])
R = int(data[1])
P = int(data[2])

total = N
new_infected = N
days = 0

while total < P:
    new_infected *= R
    total += new_infected
    days += 1

print(days)