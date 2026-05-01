import sys
import math

def main():
    data = sys.stdin.read().strip().split()
    if len(data) < 2:
        return

    A = int(data[0])  # azuis
    B = int(data[1])  # brancos

    # Se as dimensões externas são x e y, então:
    # azuis = 2x + 2y - 4
    # brancos = (x-2)(y-2)
    # Definindo u = x-2, v = y-2:
    # uv = B
    # u + v = A/2
    if A % 2 != 0:
        print("-1 -1")
        return

    s = A // 2
    delta = s * s - 4 * B
    if delta < 0:
        print("-1 -1")
        return

    r = math.isqrt(delta)
    if r * r != delta:
        print("-1 -1")
        return

    if (s - r) % 2 != 0 or (s + r) % 2 != 0:
        print("-1 -1")
        return

    u = (s - r) // 2
    v = (s + r) // 2

    if u < 0 or v < 0 or u * v != B or u + v != s:
        print("-1 -1")
        return

    x = u + 2
    y = v + 2

    if x > y:
        x, y = y, x

    print(x, y)

if __name__ == "__main__":
    main()
