import sys

data = sys.stdin.read().split()
if not data:
    exit()

A = int(data[0])
S = int(data[1])
D = int(data[2])

net_gain_per_day = S - D
if A <= S:
    print(1)
else:
    days = (A - S) // net_gain_per_day
    if (A - S) % net_gain_per_day == 0:
        days += 1
    else:
        days += 2
    print(days)