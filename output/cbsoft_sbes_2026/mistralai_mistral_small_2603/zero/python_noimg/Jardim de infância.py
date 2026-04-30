
import math

def distancia(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def produto_vetorial(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])

def angulo_agudo(p1, p2, p3):
    v1 = (p2[0]-p1[0], p2[1]-p1[1])
    v2 = (p3[0]-p1[0], p3[1]-p1[1])
    produto = v1[0]*v2[0] + v1[1]*v2[1]
    return produto > 0

def mesmo_comprimento(p1, p2, p3):
    d1 = distancia(p1, p2)
    d2 = distancia(p1, p3)
    return abs(d1 - d2) < 1e-9

def colineares(p1, p2, p3, p4):
    return abs(produto_vetorial(p1, p2, p3)) < 1e-9 and abs(produto_vetorial(p1, p2, p4)) < 1e-9

def pontos_medios_coincidentes(p1, p2, p3, p4):
    mx1 = (p1[0] + p2[0]) / 2
    my1 = (p1[1] + p2[1]) / 2
    mx2 = (p3[0] + p4[0]) / 2
    my2 = (p3[1] + p4[1]) / 2
    return abs(mx1 - mx2) < 1e-9 and abs(my1 - my2) < 1e-9

def comprimento_maior(p1, p2, p3, p4):
    d1 = distancia(p1, p2)
    d2 = distancia(p3, p4)
    return d1 > d2 + 1e-9

def perpendicular(p1, p2, p3, p4):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    v1 = (p3[0] - p1[0], p3[1] - p1[1])
    v2 = (p4[0] - p2[0], p4[1] - p2[1])
    prod1 = v1[0]*dx + v1[1]*dy
    prod2 = v2[0]*dx + v2[1]*dy
    return abs(prod1) < 1e-9 and abs(prod2) < 1e-9

def mesmo_comprimento_perpendicular(p1, p2, p3, p4):
    d1 = distancia(p1, p3)
    d2 = distancia(p2, p4)
    return abs(d1 - d2) < 1e-9

def lados_opostos_reta(p1, p2, p3, p6):
    d1 = produto_vetorial(p1, p2, p3)
    d2 = produto_vetorial(p1, p2, p6)
    return (d1 * d2) < 0

def main():
    pontos = []
    for _ in range(7):
        x, y = map(int, input().split())
        pontos.append((x, y))

    P1, P2, P3, P4, P5, P6, P7 = pontos

    condicoes = [
        angulo_agudo(P1, P2, P3),
        mesmo_comprimento(P1, P2, P3),
        colineares(P2, P3, P4, P5),
        pontos_medios_coincidentes(P2, P3, P4, P5),
        comprimento_maior(P2, P3, P4, P5),
        perpendicular(P2, P3, P4, P6),
        perpendicular(P2, P3, P5, P7),
        mesmo_comprimento_perpendicular(P4, P5, P6, P7),
        lados_opostos_reta(P2, P3, P1, P6)
    ]

    if all(condicoes):
        print("S")
    else:
        print("N")

if __name__ == "__main__":
    main()
