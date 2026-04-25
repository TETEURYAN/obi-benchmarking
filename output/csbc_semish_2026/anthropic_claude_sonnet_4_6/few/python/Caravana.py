import sys

data = sys.stdin.read().split()
n = int(data[0])
weights = [int(data[i+1]) for i in range(n)]
avg = sum(weights) // n
for w in weights:
    print(avg - w)