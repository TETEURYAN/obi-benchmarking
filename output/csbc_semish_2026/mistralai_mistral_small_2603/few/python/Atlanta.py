import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print("-1 -1")
        return
    A = int(data[0])
    B = int(data[1])

    # Equações:
    # A = 2*(L + C - 2)
    # B = (L - 2)*(C - 2)
    # Precisamos encontrar L e C >= 3 (pois precisa de pelo menos 1 fileira azul em cada lateral)
    # Reorganizando:
    # L + C = A//2 + 2
    # (L-2)*(C-2) = B

    total_blue = A
    total_white = B

    if total_blue % 2 != 0:
        print("-1 -1")
        return

    sum_LC = total_blue // 2 + 2
    product = total_white

    # Resolvendo a equação quadrática: x^2 - sum_LC*x + (product + 2*sum_LC - 4) = 0
    # Mas podemos derivar:
    # (L-2) + (C-2) = sum_LC - 4
    # (L-2)*(C-2) = product
    # Portanto, (L-2) e (C-2) são raízes de x^2 - (sum_LC-4)x + product = 0

    S = sum_LC - 4
    P = product

    # Discriminante
    D = S * S - 4 * P
    if D < 0:
        print("-1 -1")
        return

    sqrtD = int(D ** 0.5)
    if sqrtD * sqrtD != D:
        print("-1 -1")
        return

    # Raízes
    x1 = (S + sqrtD) // 2
    x2 = (S - sqrtD) // 2

    if x1 <= 0 or x2 <= 0:
        print("-1 -1")
        return

    L = x1 + 2
    C = x2 + 2

    # Garantir que L <= C
    if L > C:
        L, C = C, L

    # Verificar se as dimensões são válidas
    if 2 * (L + C - 2) == total_blue and (L - 2) * (C - 2) == total_white:
        print(f"{L} {C}")
    else:
        print("-1 -1")

if __name__ == "__main__":
    main()