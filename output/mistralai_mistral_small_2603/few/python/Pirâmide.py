
import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    if len(data) != 6:
        print('N')
        return

    weights = sorted(data)
    total = sum(weights)

    if total % 3 != 0:
        print('N')
        return

    target = total // 3
    a, b, c, d, e, f = weights

    # Verificar todas as combinações possíveis de 3 cubos para o primeiro andar
    # e os 2 cubos restantes para o segundo andar, o último para o terceiro
    # Como são apenas 6 cubos, podemos verificar todas as combinações possíveis

    # Primeiro andar: 3 cubos, segundo: 2 cubos, terceiro: 1 cubo
    # O peso do primeiro andar deve ser target, o segundo também target, e o terceiro target

    # Verificar se existe alguma combinação onde:
    # soma de 3 cubos = target, soma de 2 cubos = target, e o último cubo = target

    # Como são apenas 6 cubos, podemos gerar todas as combinações possíveis de 3 cubos
    from itertools import combinations

    for first_floor in combinations(weights, 3):
        if sum(first_floor) != target:
            continue
        remaining = [w for w in weights if w not in first_floor]
        if len(remaining) != 3:
            continue
        for second_floor in combinations(remaining, 2):
            if sum(second_floor) != target:
                continue
            third_floor = remaining[0] if remaining[1] in second_floor else remaining[1]
            if third_floor == target:
                print('S')
                return

    print('N')

if __name__ == '__main__':
    main()
