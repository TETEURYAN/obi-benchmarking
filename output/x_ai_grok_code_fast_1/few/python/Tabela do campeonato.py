import sys

J, P, V, E, D = map(int, sys.stdin.read().split())

if D == -1:
    D = J - V - E
elif J == -1:
    if E == -1:
        E = P - 3 * V
        J = V + E + D
    else:
        J = V + E + D
elif P == -1:
    P = 3 * V + E
elif V == -1:
    V = (P - E) // 3
elif E == -1:
    E = P - 3 * V

print(J, P, V, E, D)