import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n, k = data[0], data[1]
scores = data[2:2 + n]
scores.sort(reverse=True)
print(scores[k - 1])