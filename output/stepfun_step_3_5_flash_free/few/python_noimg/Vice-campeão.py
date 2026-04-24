import sys

data = sys.stdin.read().split()
if not data:
    exit()

a, b, c = map(int, data[:3])
scores = [a, b, c]
scores.sort()
print(scores[1])