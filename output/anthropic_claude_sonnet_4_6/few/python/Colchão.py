import sys

data = sys.stdin.read().split()
A, B, C = int(data[0]), int(data[1]), int(data[2])
H, L = int(data[3]), int(data[4])

dims = [A, B, C]

# The mattress is a rectangular parallelepiped. It must pass through the door
# with one face parallel to the ground. This means one dimension is the
# "thickness" lying on the ground (doesn't matter for door), and the other
# two dimensions must fit within H x L (height x width of door).
# We try all 3 choices of which dimension is the one parallel to ground (thickness),
# and for the remaining two dimensions, check if they fit in H x L.

result = False
for i in range(3):
    # dimension i is the one lying flat (thickness), doesn't constrain door
    remaining = [dims[j] for j in range(3) if j != i]
    d1, d2 = remaining[0], remaining[1]
    # Check both orientations
    if (d1 <= H and d2 <= L) or (d1 <= L and d2 <= H):
        result = True
        break

print('S' if result else 'N')