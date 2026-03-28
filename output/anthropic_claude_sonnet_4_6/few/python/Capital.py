import sys
from itertools import permutations

data = sys.stdin.read().split()
areas = list(map(int, data))

# The rectangle is divided by two lines into 4 zones.
# If we label them as:
# A B
# C D
# Then A*D == B*C (the cross-ratio condition)
# Also, A/B == C/D and A/C == B/D
# The condition is: A1*A4 == A2*A3 for some arrangement of the 4 areas.

# We need to check all permutations of the 4 areas and see if any arrangement
# satisfies the condition that opposite rectangles have equal products.
# In a 2x2 grid split by two lines:
# top-left * bottom-right == top-right * bottom-left

found = False
for perm in permutations(areas):
    a, b, c, d = perm
    # arrangement:
    # a b
    # c d
    # condition: a*d == b*c
    if a * d == b * c:
        found = True
        break

print('S' if found else 'N')