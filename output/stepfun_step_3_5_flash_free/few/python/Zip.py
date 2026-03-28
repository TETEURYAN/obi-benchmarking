import sys

def calcular_pontuacao(c1, c2):
    soma = c1 + c2
    if c1 == c2:
        return 2 * soma
    elif abs(c1 - c2) == 1:
        return 3 * soma
    else:
        return soma

dados = list(map(int, sys.stdin.read().split()))
if len(dados) < 4:
    exit()

lia_c1, lia_c2, carol_c1, carol_c2 = dados[:4]

pont_lia = calcular_pontuacao(lia_c1, lia_c2)
pont_carol = calcular_pontuacao(carol_c1, carol_c2)

if pont_lia > pont_carol:
    print("Lia")
elif pont_carol > pont_lia:
    print("Carolina")
else:
    print("empate")