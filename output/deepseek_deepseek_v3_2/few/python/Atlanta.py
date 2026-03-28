import sys
import math

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    A = int(data[0])
    B = int(data[1])

    # A = 2*(L + C) - 4
    # B = (L-2)*(C-2)
    # L >= 2, C >= 2, inteiros

    # Resolvendo o sistema:
    # De A: L + C = (A + 4) // 2
    soma = A + 4
    if soma % 2 != 0:
        print("-1 -1")
        return
    soma //= 2  # soma = L + C

    # B = (L-2)*(C-2) = L*C - 2*(L+C) + 4
    # L*C = B + 2*soma - 4
    produto_total = B + 2 * soma - 4

    # L e C são raízes de x^2 - soma*x + produto_total = 0
    delta = soma * soma - 4 * produto_total
    if delta < 0:
        print("-1 -1")
        return
    sqrt_delta = int(math.isqrt(delta))
    if sqrt_delta * sqrt_delta != delta:
        print("-1 -1")
        return

    L1 = (soma + sqrt_delta) // 2
    C1 = (soma - sqrt_delta) // 2

    # Verificar se são inteiros e positivos
    if (soma + sqrt_delta) % 2 != 0 or (soma - sqrt_delta) % 2 != 0:
        print("-1 -1")
        return

    if L1 < 2 or C1 < 2:
        print("-1 -1")
        return

    # Verificar se realmente satisfazem as equações originais
    if 2 * (L1 + C1) - 4 != A:
        print("-1 -1")
        return
    if (L1 - 2) * (C1 - 2) != B:
        print("-1 -1")
        return

    # Ordenar saída
    if L1 > C1:
        L1, C1 = C1, L1
    print(f"{L1} {C1}")

if __name__ == "__main__":
    main()