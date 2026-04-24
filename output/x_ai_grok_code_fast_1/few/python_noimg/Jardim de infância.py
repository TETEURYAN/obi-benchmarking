import sys

def eq(a, b):
    return abs(a - b) < 1e-9

def dist(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

data = list(map(int, sys.stdin.read().split()))
points = [(data[i], data[i + 1]) for i in range(0, 14, 2)]

# 1. Ângulo agudo em P1
v1 = (points[1][0] - points[0][0], points[1][1] - points[0][1])
v2 = (points[2][0] - points[0][0], points[2][1] - points[0][1])
dot = v1[0] * v2[0] + v1[1] * v2[1]
if dot <= 0:
    print("N")
    sys.exit()

# 2. P1P2 == P1P3
if not eq(dist(points[0], points[1]), dist(points[0], points[2])):
    print("N")
    sys.exit()

# 3. P2, P3, P4, P5 colineares
if not (eq(cross(points[1], points[2], points[3]), 0) and eq(cross(points[1], points[2], points[4]), 0)):
    print("N")
    sys.exit()

# 4. Meios de P2P3 e P4P5 coincidentes
mid23 = ((points[1][0] + points[2][0]) / 2, (points[1][1] + points[2][1]) / 2)
mid45 = ((points[3][0] + points[4][0]) / 2, (points[3][1] + points[4][1]) / 2)
if not (eq(mid23[0], mid45[0]) and eq(mid23[1], mid45[1])):
    print("N")
    sys.exit()

# 5. P2P3 > P4P5
if not (dist(points[1], points[2]) > dist(points[3], points[4])):
    print("N")
    sys.exit()

# 6. P4P6 e P5P7 perpendiculares a P2P3
v23 = (points[2][0] - points[1][0], points[2][1] - points[1][1])
v46 = (points[5][0] - points[3][0], points[5][1] - points[3][1])
dot46 = v23[0] * v46[0] + v23[1] * v46[1]
if not eq(dot46, 0):
    print("N")
    sys.exit()
v57 = (points[6][0] - points[4][0], points[6][1] - points[4][1])
dot57 = v23[0] * v57[0] + v23[1] * v57[1]
if not eq(dot57, 0):
    print("N")
    sys.exit()

# 7. P4P6 == P5P7
if not eq(dist(points[3], points[5]), dist(points[4], points[6])):
    print("N")
    sys.exit()

# 8. P1P6 intercepta reta P2P3 em um ponto
c1 = cross(points[1], points[2], points[0])
c2 = cross(points[1], points[2], points[5])
if not (c1 * c2 < 0):
    print("N")
    sys.exit()

print("S")