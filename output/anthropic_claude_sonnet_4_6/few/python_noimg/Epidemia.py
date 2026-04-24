import sys

data = sys.stdin.read().split()
N = int(data[0])
R = int(data[1])
P = int(data[2])

if N >= P:
    print(0)
else:
    total = N
    current = N
    days = 0
    while total < P:
        current = current * R
        total += current
        days += 1
        if R == 1 and total < P:
            # With R=1, each day same number added
            # current stays N, so days needed = ceil((P - N) / N)
            remaining = P - total
            extra_days = (remaining + current - 1) // current
            days += extra_days
            break
    print(days)