import sys

data = sys.stdin.read().split()
scores = [int(x) for x in data]

first = scores[0]
trofeus = scores.count(first)

remaining = [s for s in scores if s < first]
if remaining:
    second = remaining[0]
    placas = remaining.count(second)
else:
    placas = 0

print(trofeus, placas)