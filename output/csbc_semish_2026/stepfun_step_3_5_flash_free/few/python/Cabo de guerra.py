import sys
import itertools

dados = list(map(int, sys.stdin.read().split()))
total = sum(dados)
if total % 2 != 0:
    print('N')
else:
    alvo = total // 2
    for comb in itertools.combinations(dados, 3):
        if sum(comb) == alvo:
            print('S')
            break
    else:
        print('N')