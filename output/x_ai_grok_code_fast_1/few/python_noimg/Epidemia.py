import sys

data = sys.stdin.read().split()
N = int(data[0])
R = int(data[1])
P = int(data[2])

total = N
day = 0
current_new = N
while total < P:
    current_new *= R
    total += current_new
    day += 1
print(day)