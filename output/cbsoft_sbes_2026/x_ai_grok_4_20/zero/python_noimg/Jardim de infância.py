
import sys

input = sys.stdin.read
data = input().split()
points = []
index = 0
for i in range(7):
    x = int(data[index])
    y = int(data[index + 1])
    points.append((x, y))
    index += 2

P1 = points[0]
P2 = points[1]
P3 = points[2]
P4 = points[3]
P5 = points[4]
P6 = points[5]
P7 = points[6]

def dist2(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def dot(ax, ay, bx, by):
    return ax * bx + ay * by

def cross(ax, ay, bx, by):
    return ax * by - ay * bx

def vec(a, b):
    return (b[0] - a[0], b[1] - a[1])

# 1. Angulo P2P1P3 agudo (vertice em P1)
v12 = vec(P1, P2)
v13 = vec(P1, P3)
if dot(v12[0], v12[1], v13[0], v13[1]) >= 0:
    print("N")
    sys.exit()

# 2. P1P2 e P1P3 mesmo comprimento
if dist2(P1, P2) != dist2(P1, P3):
    print("N")
    sys.exit()

# 3. P2, P3, P4, P5 colineares
v23 = vec(P2, P3)
v24 = vec(P2, P4)
v25 = vec(P2, P5)
if cross(v23[0], v23[1], v24[0], v24[1]) != 0 or cross(v23[0], v23[1], v25[0], v25[1]) != 0:
    print("N")
    sys.exit()

# 4. Pontos medios de P2P3 e P4P5 coincidentes
mx1 = (P2[0] + P3[0]) // 2
my1 = (P2[1] + P3[1]) // 2
mx2 = (P4[0] + P5[0]) // 2
my2 = (P4[1] + P5[1]) // 2
if mx1 != mx2 or my1 != my2:
    print("N")
    sys.exit()

# 5. P2P3 > P4P5
if dist2(P2, P3) <= dist2(P4, P5):
    print("N")
    sys.exit()

# 6. P4P6 e P5P7 perpendiculares a P2P3
v46 = vec(P4, P6)
v57 = vec(P5, P7)
if dot(v23[0], v23[1], v46[0], v46[1]) != 0 or dot(v23[0], v23[1], v57[0], v57[1]) != 0:
    print("N")
    sys.exit()

# 7. P4P6 e P5P7 mesmo comprimento
if dist2(P4, P6) != dist2(P5, P7):
    print("N")
    sys.exit()

# 8. P1 e P6 separados pela reta P2P3 (segmento P1P6 intercepta a reta P2P3)
# Usamos orientacao: P1 e P6 devem estar em lados opostos da reta
o1 = cross(v23[0], v23[1], v24[0] + v12[0] - v12[0], v24[1] + v12[1] - v12[1])  # melhor: usar cross com vetores da reta
# Calculo correto de orientacao
def orientation(a, b, c):
    return cross(b[0]-a[0], b[1]-a[1], c[0]-a[0], c[1]-a[1])

oP1 = orientation(P2, P3, P1)
oP6 = orientation(P2, P3, P6)
if oP1 * oP6 >= 0:
    print("N")
    sys.exit()

print("S")
