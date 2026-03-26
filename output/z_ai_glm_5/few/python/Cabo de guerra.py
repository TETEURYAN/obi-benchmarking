import sys
from itertools import combinations

def solve():
    # Leitura rápida de todos os dados de entrada
    data = sys.stdin.read().split()
    
    # Verificação de segurança caso a entrada esteja vazia
    if not data:
        return

    # Conversão para inteiros
    forcas = list(map(int, data))
    
    # Cálculo da soma total das forças
    soma_total = sum(forcas)
    
    # Se a soma total for ímpar, é impossível dividir em dois times de soma igual
    if soma_total % 2 != 0:
        print('N')
        return
    
    # Alvo que cada time deve atingir
    alvo = soma_total // 2
    
    # Verifica todas as combinações possíveis de 3 jogadores para formar um time
    # Existem C(6, 3) = 20 combinações possíveis, o que é computacionalmente trivial
    for time in combinations(forcas, 3):
        if sum(time) == alvo:
            print('S')
            return
            
    # Se nenhuma combinação resultou na soma alvo
    print('N')

if __name__ == '__main__':
    solve()