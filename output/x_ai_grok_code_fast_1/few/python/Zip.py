import sys

input_data = sys.stdin.read().split()
a, b, c, d = map(int, input_data)

def score(x, y):
    if x == y:
        return 2 * (x + y)
    elif abs(x - y) == 1:
        return 3 * (x + y)
    else:
        return x + y

score_lia = score(a, b)
score_carolina = score(c, d)

if score_lia > score_carolina:
    print("Lia")
elif score_carolina > score_lia:
    print("Carolina")
else:
    print("empate")