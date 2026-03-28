import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    IA, IB, FA, FB = map(int, data)

    # Estados iniciais e finais
    # C1: inverte A
    # C2: inverte A e B

    # Queremos minimizar o número de apertos.
    # Vamos testar as 4 combinações de paridade de apertos de C1 e C2.
    # Seja x = número de vezes que apertamos C1 (mod 2)
    # Seja y = número de vezes que apertamos C2 (mod 2)
    # Então:
    # A final = IA ^ x ^ y   (pois C1 e C2 afetam A)
    # B final = IB ^ y       (pois só C2 afeta B)
    # Queremos IA ^ x ^ y == FA  e  IB ^ y == FB
    # Da segunda: y = IB ^ FB
    # Substituindo na primeira: IA ^ x ^ (IB ^ FB) == FA
    # Logo x = IA ^ IB ^ FB ^ FA
    # x e y são 0 ou 1 (mod 2). Se x=1, apertamos C1 ímpar vezes (pelo menos 1).
    # Se y=1, apertamos C2 ímpar vezes (pelo menos 1).
    # Mas podemos combinar apertos: se ambos forem 1, podemos apertar C1 e C2 (2 apertos)
    # ou apertar C1 e C2 uma vez cada? Na verdade, a ordem não importa, só a paridade.
    # O número mínimo de apertos é:
    # - Se x=0 e y=0 -> 0
    # - Se x=1 e y=0 -> 1 (só C1)
    # - Se x=0 e y=1 -> 1 (só C2)
    # - Se x=1 e y=1 -> 2 (C1 e C2, ou C2 e C1, mas não dá para fazer em 1 aperto)
    # Mas cuidado: existe a possibilidade de fazer em 1 aperto se apertarmos C2?
    # C2 inverte A e B. Se precisamos inverter A e B, mas não simultaneamente, talvez dê.
    # Vamos testar todas as possibilidades de 0,1,2 apertos.

    best = 10**9
    # Testar 0 apertos
    if IA == FA and IB == FB:
        best = 0

    # Testar 1 aperto
    # C1
    if (IA ^ 1) == FA and IB == FB:
        best = min(best, 1)
    # C2
    if (IA ^ 1) == FA and (IB ^ 1) == FB:
        best = min(best, 1)

    # Testar 2 apertos
    # C1 + C1 = nada, já coberto
    # C2 + C2 = nada, já coberto
    # C1 + C2
    if (IA ^ 1 ^ 1) == FA and (IB ^ 1) == FB:  # C1 inverte A, C2 inverte A e B
        # A: IA -> IA^1 (C1) -> IA^1^1 (C2) = IA
        # B: IB -> IB^1 (C2)
        # Então final: (IA, IB^1)
        # Mas isso é igual a apertar só C2? Não, porque C2 sozinho dá (IA^1, IB^1).
        # Vamos calcular corretamente:
        # A após C1: IA^1
        # A após C2: (IA^1)^1 = IA
        # B após C1: IB
        # B após C2: IB^1
        # Então final: (IA, IB^1)
        # Isso é igual a apertar só C2? Só C2 dá (IA^1, IB^1). Diferente.
        # Portanto, é uma configuração distinta.
        if IA == FA and (IB ^ 1) == FB:
            best = min(best, 2)
    # C2 + C1 (mesmo que C1 + C2, comutativo)
    if (IA ^ 1 ^ 1) == FA and (IB ^ 1) == FB:  # mesmo cálculo
        if IA == FA and (IB ^ 1) == FB:
            best = min(best, 2)

    # Outras combinações de 2 apertos: C1 + C1 já é 0, C2 + C2 já é 0.
    # Mas também podemos apertar C1 duas vezes? Isso não muda nada.
    # Portanto, só precisamos verificar as combinações acima.

    # Se não encontrou até agora, pode ser 2 apertos de outra forma?
    # Na verdade, com 2 interruptores binários, o máximo de estados alcançáveis
    # com até 2 apertos é coberto. Se não deu, tenta 3? Mas o mínimo será no máximo 2.
    # Porque com 2 interruptores, o espaço de estados é 4, e qualquer transição
    # pode ser feita em no máximo 2 apertos (isso é um fato conhecido).
    # Vamos garantir com brute force para 0,1,2 apertos.

    # Mas já fizemos brute force para 0 e 1. Para 2, as possibilidades são:
    # (C1,C1), (C2,C2), (C1,C2), (C2,C1). As duas primeiras são equivalentes a 0.
    # As duas últimas são equivalentes entre si. Então só testamos uma.
    # Já testamos (C1,C2) acima. Então está completo.

    print(best)

if __name__ == "__main__":
    solve()