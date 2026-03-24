import sys

data = list(map(int, sys.stdin.read().split()))
J, P, V, E, D = data

if J == -1:
    J = V + E + D
elif P == -1:
    P = 3 * V + E
elif V == -1:
    V = (P - E) // 3
elif E == -1:
    E = P - 3 * V
elif D == -1:
    D = J - V - E

if J == -1:
    J = V + E + D
if P == -1:
    P = 3 * V + E
if V == -1:
    V = J - E - D
if E == -1:
    E = J - V - D
if D == -1:
    D = J - V - E

if P == -1:
    P = 3 * V + E
if V == -1:
    V = (P - E) // 3
if E == -1:
    E = P - 3 * V

print(J, P, V, E, D)