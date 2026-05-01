A = int(input())
B = int(input())

# Starting from chair 1, counting A chairs anti-clockwise
# Chairs in anti-clockwise order starting from 1: 1, 2, 0, 1, 2, 0, ...
# Starting at chair 1, after A steps: chair = (1 + A - 1) % 3 = A % 3
# Wait, let's think: starting from chair 1, count 1 -> chair 1, count 2 -> chair 2, count 3 -> chair 0
# So after A counts: chair = (1 + (A-1)) % 3 = A % 3

ana_chair = A % 3

# Beatriz does the same
bea_chair = B % 3
if bea_chair == ana_chair:
    bea_chair = (bea_chair + 1) % 3

# Carolina gets the remaining chair
all_chairs = {0, 1, 2}
carolina_chair = (all_chairs - {ana_chair, bea_chair}).pop()

print(carolina_chair)