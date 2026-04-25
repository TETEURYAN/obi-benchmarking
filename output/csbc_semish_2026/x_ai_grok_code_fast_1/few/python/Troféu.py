import sys

data = sys.stdin.read().split()
P = [int(x) for x in data]

trofeus = 0
for i in range(5):
    if P[i] == P[0]:
        trofeus += 1
    else:
        break

if trofeus == 5:
    placas = 0
else:
    placas = 0
    for i in range(trofeus, 5):
        if P[i] == P[trofeus]:
            placas += 1
        else:
            break

print(trofeus, placas)