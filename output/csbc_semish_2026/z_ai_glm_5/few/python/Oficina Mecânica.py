import sys
import heapq

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # Iterador para processar os tokens de forma sequencial
    iterator = iter(input_data)
    
    try:
        N = int(next(iterator))
        M = int(next(iterator))
    except StopIteration:
        return

    # Leitura dos tempos base dos carros
    T = []
    for _ in range(N):
        try:
            T.append(int(next(iterator)))
        except StopIteration:
            break
            
    # Leitura dos fatores de trabalho dos mecânicos
    F = []
    for _ in range(M):
        try:
            F.append(int(next(iterator)))
        except StopIteration:
            break

    # Ordenar os carros em ordem decrescente de tempo base.
    # Isso garante que carros com maior tempo base sejam atribuídos aos "slots" 
    # com menor multiplicador de espera (coeficiente), minimizando a soma total.
    T.sort(reverse=True)

    # Inicializa a fila de prioridade (min-heap).
    # Cada elemento é uma tupla (coeficiente_atual, fator_mecanico).
    # O coeficiente_atual representa o multiplicador k para o próximo carro atribuído a este mecânico.
    # Inicialmente, para todo mecânico j, o primeiro carro tem coeficiente 0 (espera 0).
    heap = [(0, f) for f in F]
    heapq.heapify(heap)

    total_wait_time = 0

    # Atribuir cada carro ao mecânico que oferece o menor custo incremental de espera
    for t in T:
        # Extrai o mecânico com menor coeficiente atual
        coeff, f_val = heapq.heappop(heap)
        
        # Adiciona o tempo de espera deste carro à soma total
        # Tempo de espera = coeficiente * tempo_base * fator
        # Nota: O problema define tempo de espera como a soma dos tempos de conserto dos carros anteriores.
        # Se um mecânico já processou k carros, o próximo carro espera a soma dos tempos daqueles k carros.
        # O coeficiente 'coeff' acumula essa lógica de forma simplificada.
        total_wait_time += coeff * t
        
        # Atualiza o estado do mecânico e reinsere na heap.
        # O novo coeficiente será coeff + f_val.
        # Isso representa que o próximo carro terá que esperar o carro atual (t * f_val) a mais.
        heapq.heappush(heap, (coeff + f_val, f_val))

    print(total_wait_time)

if __name__ == '__main__':
    solve()