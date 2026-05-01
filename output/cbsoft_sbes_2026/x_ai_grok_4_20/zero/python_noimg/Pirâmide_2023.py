
from itertools import combinations

pesos = list(map(int, input().split()))
total = sum(pesos)

if total % 3 != 0:
    print('N')
else:
    alvo = total // 3
    pesos.sort()
    
    # Verifica se o maior cubo excede o alvo
    if pesos[-1] > alvo:
        print('N')
    else:
        encontrado = False
        # Tenta encontrar combinação de 3 para o topo (andar 3)
        for comb3 in combinations(pesos, 3):
            if sum(comb3) == alvo:
                resto = [x for x in pesos if x not in comb3][:3]  # pega os 3 restantes
                if sum(resto) == 2 * alvo:
                    # Agora verifica se os 3 restantes podem ser divididos em dois grupos de soma alvo
                    r = sorted(resto)
                    if r[0] + r[1] == alvo and r[2] == alvo:
                        encontrado = True
                        break
                    if r[0] + r[2] == alvo and r[1] == alvo:
                        encontrado = True
                        break
                    if r[1] + r[2] == alvo and r[0] == alvo:
                        encontrado = True
                        break
        if encontrado:
            print('S')
        else:
            print('N')
