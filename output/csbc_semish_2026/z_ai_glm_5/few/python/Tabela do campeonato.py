
import sys

J, P, V, E, D = map(int, sys.stdin.read().split())

missing_count = sum(1 for x in [J, P, V, E, D] if x == -1)

if missing_count == 1:
    if J == -1:
        J = V + E + D
    elif P == -1:
        P = 3 * V + E
    elif V == -1:
        V = (P - E) // 3
    elif E == -1:
        E = P - 3 * V
    else:
        D = J - V - E
else:
    if J == -1 and P == -1:
        J = V + E + D
        P = 3 * V + E
    elif J == -1 and V == -1:
        V = (P - E) // 3
        J = V + E + D
    elif J == -1 and E == -1:
        E = P - 3 * V
        J = V + E + D
    elif P == -1 and V == -1:
        V = J - E - D
        P = 3 * V + E
    elif P == -1 and E == -1:
        E = J - V - D
        P = 3 * V + E
    elif P == -1 and D == -1:
        D = J - V - E
        P = 3 * V + E
    elif V == -1 and E == -1:
        V = (P - J + D) // 2
        E = P - 3 * V
    elif V == -1 and D == -1:
        V = (P - E) // 3
        D = J - V - E
    else:
        E = P - 3 * V
        D = J - V - E

print(J, P, V, E, D)
