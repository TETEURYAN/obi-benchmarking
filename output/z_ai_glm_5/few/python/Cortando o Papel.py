import sys

# Aumentar o limite de recursão, embora a solução seja iterativa.
sys.setrecursionlimit(200000)

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
    except StopIteration:
        return

    A = []
    for _ in range(n):
        try:
            A.append(int(next(iterator)))
        except StopIteration:
            break
            
    if n == 0:
        print(1)
        return

    # Criar lista de eventos (altura, índice)
    events = []
    for i in range(n):
        events.append((A[i], i))
    
    # Ordenar eventos por altura
    events.sort()
    
    # Inicialmente, todos os retângulos estão "ativos" (corte em H=0).
    # Existe apenas 1 segmento contínuo.
    current_segments = 1
    max_segments = 1
    
    idx = 0
    while idx < n:
        current_height = events[idx][0]
        
        # Coletar todos os índices com a altura atual
        indices = []
        while idx < n and events[idx][0] == current_height:
            indices.append(events[idx][1])
            idx += 1
        
        # Os índices já vêm ordenados devido à ordenação dos eventos
        
        # Processar os blocos contínuos de índices
        j = 0
        while j < len(indices):
            start_block = indices[j]
            end_block = start_block
            
            # Encontrar o fim do bloco contínuo
            k = j + 1
            while k < len(indices) and indices[k] == indices[k-1] + 1:
                end_block = indices[k]
                k += 1
            
            # Verificar vizinhos
            # Vizinho à esquerda
            left_active = False
            if start_block > 0:
                if A[start_block - 1] > current_height:
                    left_active = True
            
            # Vizinho à direita
            right_active = False
            if end_block < n - 1:
                if A[end_block + 1] > current_height:
                    right_active = True
            
            # Calcular a mudança no número de segmentos
            if left_active and right_active:
                # O bloco conectava dois segmentos -> remoção divide em dois
                current_segments += 1
            elif not left_active and not right_active:
                # O bloco era um segmento isolado -> remoção elimina o segmento
                current_segments -= 1
            # Se apenas um lado está ativo, o segmento encolhe, contagem não muda
            
            # Atualizar máximo
            if current_segments > max_segments:
                max_segments = current_segments
            
            j = k

    # O número de pedaços é 1 (parte de baixo) + número de segmentos (partes de cima)
    print(max_segments + 1)

if __name__ == '__main__':
    solve()