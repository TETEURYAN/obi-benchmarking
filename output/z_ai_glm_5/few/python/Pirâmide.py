import sys
import itertools

def solve():
    # Leitura rápida dos dados de entrada
    data = sys.stdin.read().split()
    
    # Verificação de segurança caso a entrada esteja vazia
    if not data:
        return

    # Conversão para inteiros
    cubes = list(map(int, data))
    
    # Cálculo do peso total
    total_sum = sum(cubes)
    
    # Condição necessária: o peso total deve ser divisível por 3
    if total_sum % 3 != 0:
        print('N')
        return
    
    target = total_sum // 3
    
    # Iterar por todas as combinações de 3 cubos para o primeiro andar
    # Usamos índices para evitar problemas com pesos duplicados
    for indices_f1 in itertools.combinations(range(6), 3):
        sum_f1 = sum(cubes[i] for i in indices_f1)
        
        if sum_f1 == target:
            # Identificar os cubos restantes
            remaining_indices = [i for i in range(6) if i not in indices_f1]
            remaining_cubes = [cubes[i] for i in remaining_indices]
            
            # Iterar por todas as combinações de 2 cubos restantes para o segundo andar
            for indices_f2 in itertools.combinations(range(3), 2):
                sum_f2 = sum(remaining_cubes[i] for i in indices_f2)
                
                if sum_f2 == target:
                    # Se o primeiro e segundo andar somam 'target', o terceiro (restante) também somará
                    print('S')
                    return
                    
    # Se nenhuma combinação válida for encontrada
    print('N')

if __name__ == '__main__':
    solve()