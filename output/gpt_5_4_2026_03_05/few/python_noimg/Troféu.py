import sys

scores = list(map(int, sys.stdin.read().split()))

trophies = 1
while trophies < 5 and scores[trophies] == scores[0]:
    trophies += 1

if trophies == 5:
    plaques = 0
else:
    plaques = 1
    second_score = scores[trophies]
    while trophies + plaques < 5 and scores[trophies + plaques] == second_score:
        plaques += 1

print(trophies, plaques)