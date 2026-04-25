import sys

input_data = sys.stdin.read().split()

if not input_data:
    exit()

scores = list(map(int, input_data))

max_score = scores[0]

trophies = 0
for score in scores:
    if score == max_score:
        trophies += 1
    else:
        break

plaques = 0
if trophies < 5:
    second_max_score = scores[trophies]
    for i in range(trophies, 5):
        if scores[i] == second_max_score:
            plaques += 1
        else:
            break

print(trophies, plaques)