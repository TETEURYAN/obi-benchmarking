import sys

data = sys.stdin.read().split()
vals = [int(x) for x in data]
J, P, V, E, D = vals

# We have two equations:
# J = V + E + D
# P = 3*V + E
# And one or two unknowns among J, P, V, E, D

# Try all combinations for the unknowns
unknowns = [i for i in range(5) in range(5) if vals[i] == -1]

# Find which indices are unknown
unknown_indices = [i for i in range(5) if vals[i] == -1]

# Brute force: try all possible values
# J in [1,100], P in [0,300], V in [0,100], E in [0,100], D in [0,100]
ranges = [range(1, 101), range(0, 301), range(0, 101), range(0, 101), range(0, 101)]

if len(unknown_indices) == 1:
    idx = unknown_indices[0]
    for v in ranges[idx]:
        candidate = vals[:]
        candidate[idx] = v
        J2, P2, V2, E2, D2 = candidate
        if J2 == V2 + E2 + D2 and P2 == 3*V2 + E2:
            print(J2, P2, V2, E2, D2)
            break
else:
    idx1, idx2 = unknown_indices
    found = False
    for v1 in ranges[idx1]:
        if found:
            break
        for v2 in ranges[idx2]:
            candidate = vals[:]
            candidate[idx1] = v1
            candidate[idx2] = v2
            J2, P2, V2, E2, D2 = candidate
            if J2 == V2 + E2 + D2 and P2 == 3*V2 + E2:
                print(J2, P2, V2, E2, D2)
                found = True
                break