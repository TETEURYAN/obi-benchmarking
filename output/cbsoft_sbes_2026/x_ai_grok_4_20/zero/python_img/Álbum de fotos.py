
import sys

input = sys.stdin.read
data = input().split()

X = int(data[0])
Y = int(data[1])
L1 = int(data[2])
H1 = int(data[3])
L2 = int(data[4])
H2 = int(data[5])

def can_fit(a, b, c, d):
    return (a + c <= X and max(b, d) <= Y) or (a + d <= X and max(b, c) <= Y) or \
           (b + c <= X and max(a, d) <= Y) or (b + d <= X and max(a, c) <= Y)

possible = False

# Foto 1 sem rotação, Foto 2 em 4 orientações
if can_fit(L1, H1, L2, H2) or can_fit(L1, H1, H2, L2):
    possible = True

# Foto 1 rotacionada, Foto 2 em 4 orientações
if can_fit(H1, L1, L2, H2) or can_fit(H1, L1, H2, L2):
    possible = True

# Verificar também lado a lado na outra dimensão (vertical)
if (max(L1, L2) <= X and H1 + H2 <= Y) or (max(L1, H2) <= X and H1 + L2 <= Y) or \
   (max(H1, L2) <= X and L1 + H2 <= Y) or (max(H1, H2) <= X and L1 + L2 <= Y):
    possible = True

if possible:
    print('S')
else:
    print('N')
