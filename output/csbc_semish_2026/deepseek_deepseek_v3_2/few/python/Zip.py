import sys

def score(a, b):
    if a == b:
        return 2 * (a + b)
    if abs(a - b) == 1:
        return 3 * (a + b)
    return a + b

data = sys.stdin.read().strip().split()
if len(data) != 4:
    exit()

lia1, lia2, carolina1, carolina2 = map(int, data)

score_lia = score(lia1, lia2)
score_carolina = score(carolina1, carolina2)

if score_lia > score_carolina:
    print("Lia")
elif score_carolina > score_lia:
    print("Carolina")
else:
    print("empate")