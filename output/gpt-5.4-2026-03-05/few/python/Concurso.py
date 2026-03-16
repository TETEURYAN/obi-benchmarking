import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    exit()

n, k = data[0], data[1]
scores = data[2:2 + n]

scores.sort(reverse=True)

if k == 0:
    print(101)
else:
    print(scores[k - 1])