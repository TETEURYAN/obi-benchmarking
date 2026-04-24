
import sys

def main():
    data = sys.stdin.read().split()
    J, P, V, E, D = map(int, data)

    if J == -1:
        if V != -1 and E != -1 and D != -1:
            J = V + E + D
        elif P != -1 and V != -1 and E != -1:
            J = (P - E) // 3 + E + D
        elif P != -1 and V != -1 and D != -1:
            J = V + (P - 3 * V) + D
        elif P != -1 and E != -1 and D != -1:
            J = (P - E) // 3 + E + D
        else:
            J = V + E + D

    if P == -1:
        P = 3 * V + E

    if V == -1:
        if J != -1 and E != -1 and D != -1:
            V = J - E - D
        elif P != -1 and E != -1:
            V = (P - E) // 3
        elif P != -1 and D != -1:
            V = (P - (J - V - D)) // 3

    if E == -1:
        if J != -1 and V != -1 and D != -1:
            E = J - V - D
        elif P != -1 and V != -1:
            E = P - 3 * V

    if D == -1:
        if J != -1 and V != -1 and E != -1:
            D = J - V - E

    print(f"{J} {P} {V} {E} {D}")

if __name__ == "__main__":
    main()
