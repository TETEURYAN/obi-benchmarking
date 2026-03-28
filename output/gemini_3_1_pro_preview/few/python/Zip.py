import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

l1 = int(input_data[0])
l2 = int(input_data[1])
c1 = int(input_data[2])
c2 = int(input_data[3])

def get_score(a, b):
    if a == b:
        return 2 * (a + b)
    elif abs(a - b) == 1:
        return 3 * (a + b)
    else:
        return a + b

score_lia = get_score(l1, l2)
score_carolina = get_score(c1, c2)

if score_lia > score_carolina:
    print("Lia")
elif score_carolina > score_lia:
    print("Carolina")
else:
    print("empate")