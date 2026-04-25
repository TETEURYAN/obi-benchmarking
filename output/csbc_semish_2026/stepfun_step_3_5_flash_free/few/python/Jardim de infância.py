import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    coords = list(map(int, data))
    points = [(coords[2*i], coords[2*i+1]) for i in range(7)]
    P1, P2, P3, P4, P5, P6, P7 = points

    def dist2(a, b):
        dx = a[0] - b[0]
        dy = a[1] - b[1]
        return dx*dx + dy*dy

    def dot(u, v):
        return u[0]*v[0] + u[1]*v[1]

    def cross(u, v):
        return u[0]*v[1] - u[1]*v[0]

    if dist2(P1, P2) != dist2(P1, P3):
        print('N')
        return

    v12 = (P2[0]-P1[0], P2[1]-P1[1])
    v13 = (P3[0]-P1[0], P3[1]-P1[1])
    if dot(v12, v13) <= 0:
        print('N')
        return

    v = (P3[0]-P2[0], P3[1]-P2[1])

    v24 = (P4[0]-P2[0], P4[1]-P2[1])
    v25 = (P5[0]-P2[0], P5[1]-P2[1])
    if cross(v24, v) != 0 or cross(v25, v) != 0:
        print('N')
        return

    if P2[0]+P3[0] != P4[0]+P5[0] or P2[1]+P3[1] != P4[1]+P5[1]:
        print('N')
        return

    if dist2(P2, P3) <= dist2(P4, P5):
        print('N')
        return

    v46 = (P6[0]-P4[0], P6[1]-P4[1])
    v57 = (P7[0]-P5[0], P7[1]-P5[1])
    if dot(v46, v) != 0 or dot(v57, v) != 0:
        print('N')
        return

    if dist2(P4, P6) != dist2(P5, P7):
        print('N')
        return

    v1 = (P1[0]-P2[0], P1[1]-P2[1])
    v6 = (P6[0]-P2[0], P6[1]-P2[1])
    c1 = cross(v1, v)
    c6 = cross(v6, v)
    if c1 == 0 or c6 == 0 or c1 * c6 >= 0:
        print('N')
        return

    print('S')

if __name__ == "__main__":
    main()