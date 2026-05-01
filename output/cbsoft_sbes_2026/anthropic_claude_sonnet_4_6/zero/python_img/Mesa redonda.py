A = int(input())
B = int(input())

# Starting from chair 1, counting A chairs anti-clockwise
# Chairs in anti-clockwise order starting from 1: 1, 2, 0, 1, 2, 0, ...
# The sequence starting from chair 1 going anti-clockwise is: 1, 2, 0, 1, 2, 0...
# After counting A steps starting from chair 1:
# position = (1 + A - 1) % 3 = A % 3... let's verify
# A=8: (1 + 8 - 1) % 3 = 8 % 3 = 2 ✓
# A=3: (1 + 3 - 1) % 3 = 3 % 3 = 0 ✓

ana_chair = (A % 3)  # same as (1 + A - 1) % 3

bea_chair = (B % 3)
if bea_chair == ana_chair:
    bea_chair = (bea_chair + 1) % 3

# Carolina sits in the remaining chair
all_chairs = {0, 1, 2}
carolina_chair = (all_chairs - {ana_chair, bea_chair}).pop()

print(carolina_chair)