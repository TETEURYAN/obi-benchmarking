import sys

data = sys.stdin.read().split()
A = int(data[0])
B = int(data[1])
R = int(data[2])
G = int(data[3])

# Check box: pizza (diameter 2R) must fit in box (A x B)
# The pizza fits if min(A,B) >= 2R and max(A,B) >= 2R, i.e., both dimensions >= 2R
box_ok = (A >= 2 * R) and (B >= 2 * R)

# Check angle: 360 must be divisible by G
angle_ok = (360 % G == 0)

if box_ok and angle_ok:
    print("S")
else:
    print("N")