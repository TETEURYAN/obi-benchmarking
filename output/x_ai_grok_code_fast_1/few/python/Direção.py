import sys

directions = {
    "norte": 0,
    "leste": 90,
    "sul": 180,
    "oeste": 270
}

data = sys.stdin.read().split()
A = data[0]
B = data[1]

angle_a = directions[A]
angle_b = directions[B]
diff = abs(angle_a - angle_b)
min_angle = min(diff, 360 - diff)

print(min_angle)