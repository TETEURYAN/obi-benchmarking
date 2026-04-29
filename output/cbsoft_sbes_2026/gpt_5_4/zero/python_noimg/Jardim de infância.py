import sys

pts = [tuple(map(int, sys.stdin.readline().split())) for _ in range(7)]
P1, P2, P3, P4, P5, P6, P7 = pts

def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])

def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]

def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]

def dist2(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return dx * dx + dy * dy

ok = True

# 1) ângulo P2P1P3 agudo
v12 = sub(P2, P1)
v13 = sub(P3, P1)
if dot(v12, v13) <= 0:
    ok = False

# 2) P1P2 == P1P3
if ok and dist2(P1, P2) != dist2(P1, P3):
    ok = False

# 3) P2, P3, P4, P5 colineares
base = sub(P3, P2)
if ok and (cross(base, sub(P4, P2)) != 0 or cross(base, sub(P5, P2)) != 0):
    ok = False

# garantir que P2 != P3 (já são distintos, mas mantém robustez)
if ok and base == (0, 0):
    ok = False

# 4) pontos médios de P2P3 e P4P5 coincidentes
if ok and (P2[0] + P3[0] != P4[0] + P5[0] or P2[1] + P3[1] != P4[1] + P5[1]):
    ok = False

# 5) |P2P3| > |P4P5|
if ok and dist2(P2, P3) <= dist2(P4, P5):
    ok = False

# 6) P4P6 e P5P7 perpendiculares a P2P3
v46 = sub(P6, P4)
v57 = sub(P7, P5)
if ok and (dot(v46, base) != 0 or dot(v57, base) != 0):
    ok = False

# 7) P4P6 == P5P7
if ok and dist2(P4, P6) != dist2(P5, P7):
    ok = False

# 8) P1 e P6 separados pela reta de P2P3:
# segmento P1P6 intercepta a reta em um único ponto <=> lados opostos estritos
if ok:
    c1 = cross(base, sub(P1, P2))
    c6 = cross(base, sub(P6, P2))
    if c1 == 0 or c6 == 0 or c1 * c6 >= 0:
        ok = False

print("S" if ok else "N")