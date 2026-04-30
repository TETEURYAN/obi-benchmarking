
from itertools import combinations

pesos = list(map(int, input().split()))
total = sum(pesos)

if total % 3 != 0:
    print('N')
else:
    alvo = total // 3
    pesos.sort()
    
    # Verifica se o maior cubo excede o alvo (não pode ser colocado no topo)
    if pesos[-1] > alvo:
        print('N')
    else:
        # Tenta encontrar combinação de 3 cubos que somem ao alvo (base)
        found = False
        for comb3 in combinations(range(6), 3):
            s3 = pesos[comb3[0]] + pesos[comb3[1]] + pesos[comb3[2]]
            if s3 == alvo:
                remaining = [pesos[i] for i in range(6) if i not in comb3]
                # Verifica se os 3 restantes podem formar dois que somam ao alvo
                for i in range(3):
                    for j in range(i+1, 3):
                        if remaining[i] + remaining[j] == alvo:
                            found = True
                            break
                    if found:
                        break
                if found:
                    break
        print('S' if found else 'N')
