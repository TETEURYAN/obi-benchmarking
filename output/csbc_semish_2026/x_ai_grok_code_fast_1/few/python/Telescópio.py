import sys

data = sys.stdin.read().split()
A = int(data[0])
N = int(data[1])
fluxos = [int(x) for x in data[2:2+N]]
count = 0
for f in fluxos:
    if A * f >= 40000000:
        count += 1
print(count)