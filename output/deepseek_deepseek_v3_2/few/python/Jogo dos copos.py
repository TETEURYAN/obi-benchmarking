import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])
initial = data[1]

cup = initial  # posição da moeda: 'A', 'B' ou 'C'

idx = 2
for _ in range(n):
    move = int(data[idx])
    idx += 1
    if move == 1:
        if cup == 'A':
            cup = 'B'
        elif cup == 'B':
            cup = 'A'
    elif move == 2:
        if cup == 'B':
            cup = 'C'
        elif cup == 'C':
            cup = 'B'
    elif move == 3:
        if cup == 'A':
            cup = 'C'
        elif cup == 'C':
            cup = 'A'

sys.stdout.write(cup + '\n')