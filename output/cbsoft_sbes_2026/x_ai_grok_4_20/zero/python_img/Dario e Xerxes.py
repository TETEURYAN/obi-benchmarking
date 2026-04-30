
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
index = 1

wins_dario = 0
wins_xerxes = 0

for i in range(N):
    D = int(data[index])
    X = int(data[index + 1])
    index += 2
    
    # Verifica se Xerxes ganha (seta de X para D)
    if (X == 0 and D == 1) or \
       (X == 1 and D == 2) or \
       (X == 2 and D == 3) or \
       (X == 3 and D == 4) or \
       (X == 4 and D == 0) or \
       (X == 0 and D == 2) or \
       (X == 1 and D == 3) or \
       (X == 2 and D == 4) or \
       (X == 3 and D == 0) or \
       (X == 4 and D == 1):
        wins_xerxes += 1
    else:
        wins_dario += 1

if wins_dario > wins_xerxes:
    print("dario")
else:
    print("xerxes")
