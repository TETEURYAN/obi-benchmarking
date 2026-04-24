import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    A, B, C, D, E, F, G = (int(next(it)) for _ in range(7))

    # Princípio da Inclusão-Exclusão para três conjuntos
    # |A ∪ B ∪ C| = |A| + |B| + |C| - |A∩B| - |A∩C| - |B∩C| + |A∩B∩C|
    # Sabemos que |A ∪ B ∪ C| = N - G (pessoas que praticam pelo menos um esporte)
    # Seja X = |A∩B∩C| (o que queremos descobrir se é > 0)
    # Então: N - G = A + B + C - D - E - F + X
    # Portanto: X = N - G - (A + B + C - D - E - F)
    # Se X > 0, então há alguém que pratica três esportes.

    total_pelo_menos_um = N - G
    soma_individual = A + B + C
    soma_duplas = D + E + F
    X = total_pelo_menos_um - (soma_individual - soma_duplas)

    print("S" if X > 0 else "N")

if __name__ == "__main__":
    solve()