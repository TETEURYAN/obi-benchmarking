
import sys

input = sys.stdin.read
data = input().split()

X = int(data[0])
Y = int(data[1])
L1 = int(data[2])
H1 = int(data[3])
L2 = int(data[4])
H2 = int(data[5])

# Todas as 4 combinações de rotação para cada foto
dims1 = [(L1, H1), (H1, L1)]
dims2 = [(L2, H2), (H2, L2)]

possible = False

for w1, h1 in dims1:
    for w2, h2 in dims2:
        # Tentativa 1: lado a lado horizontalmente
        if w1 + w2 <= X and max(h1, h2) <= Y:
            possible = True
        # Tentativa 2: uma em cima da outra verticalmente
        if max(w1, w2) <= X and h1 + h2 <= Y:
            possible = True

if possible:
    print('S')
else:
    print('N')
