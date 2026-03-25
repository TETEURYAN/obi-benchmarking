import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

A, B, R, G = map(int, data)

ok_box = (2 * R <= A and 2 * R <= B)
ok_angle = (360 % G == 0)

print('S' if ok_box and ok_angle else 'N')