import sys
import array

# Definir limite de recursão, embora não seja utilizado nesta solução iterativa
sys.setrecursionlimit(200000)

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        N = int(next(iterator))
        Q = int(next(iterator))
    except StopIteration:
        return

    MAX_R = 50
    # Tamanho do BIT: índices de 1 a Q+1 (mapeamento tempo -> índice)
    BIT_SIZE = Q + 2
    
    # Estado das linhas e colunas
    # row_time[i] guarda o tempo da última atualização da linha i
    # row_val[i] guarda o valor definido na última atualização
    # Inicialmente, tempo 0 e valor 0
    row_time = [0] * (N + 1)
    row_val = [0] * (N + 1)
    col_time = [0] * (N + 1)
    col_val = [0] * (N + 1)
    
    # BITs para contagem de timestamps
    # row_time_bit: conta quantas linhas foram atualizadas em cada tempo t
    # col_time_bit: conta quantas colunas foram atualizadas em cada tempo t
    # Usamos array('i') para economizar memória (inteiros de 4 bytes)
    row_time_bit = array.array('i', [0] * BIT_SIZE)
    col_time_bit = array.array('i', [0] * BIT_SIZE)
    
    # BITs para contagem de valores por timestamp
    # row_val_bit[r]: conta quantas linhas com valor r foram atualizadas em cada tempo t
    # col_val_bit[r]: conta quantas colunas com valor r foram atualizadas em cada tempo t
    row_val_bits = [array.array('i', [0] * BIT_SIZE) for _ in range(MAX_R + 1)]
    col_val_bits = [array.array('i', [0] * BIT_SIZE) for _ in range(MAX_R + 1)]
    
    # Contadores totais para otimização
    # row_total_counts[r]: total de linhas com valor atual r
    row_total_counts = [0] * (MAX_R + 1)
    col_total_counts = [0] * (MAX_R + 1)
    
    # Funções auxiliares para BIT (definidas localmente para capturar BIT_SIZE)
    def update(bit, i, delta):
        while i < BIT_SIZE:
            bit[i] += delta
            i += i & (-i)
    
    def query(bit, i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & (-i)
        return s

    # Inicialização: Todas as N linhas e N colunas têm valor 0 no tempo 0
    # Tempo 0 mapeia para índice 1 no BIT
    update(row_time_bit, 1, N)
    update(col_time_bit, 1, N)
    update(row_val_bits[0], 1, N)
    update(col_val_bits[0], 1, N)
    row_total_counts[0] = N
    col_total_counts[0] = N
    
    output_buffer = []
    
    # Processar Q operações
    # k é o tempo atual (1 a Q)
    for k in range(1, Q + 1):
        op = int(next(iterator))
        
        if op == 1:
            # Atribuir valor R à linha X
            X = int(next(iterator))
            R = int(next(iterator))
            
            old_t = row_time[X]
            old_v = row_val[X]
            
            # Remover estado antigo dos BITs
            idx_old = old_t + 1
            update(row_time_bit, idx_old, -1)
            update(row_val_bits[old_v], idx_old, -1)
            row_total_counts[old_v] -= 1
            
            # Adicionar novo estado
            row_time[X] = k
            row_val[X] = R
            idx_new = k + 1
            update(row_time_bit, idx_new, 1)
            update(row_val_bits[R], idx_new, 1)
            row_total_counts[R] += 1
            
        elif op == 2:
            # Atribuir valor R à coluna X
            X = int(next(iterator))
            R = int(next(iterator))
            
            old_t = col_time[X]
            old_v = col_val[X]
            
            idx_old = old_t + 1
            update(col_time_bit, idx_old, -1)
            update(col_val_bits[old_v], idx_old, -1)
            col_total_counts[old_v] -= 1
            
            col_time[X] = k
            col_val[X] = R
            idx_new = k + 1
            update(col_time_bit, idx_new, 1)
            update(col_val_bits[R], idx_new, 1)
            col_total_counts[R] += 1
            
        elif op == 3:
            # Imprimir valor mais frequente na linha X
            X = int(next(iterator))
            
            t_row = row_time[X]
            v_row = row_val[X]
            
            # Índice limite para consulta (tempo <= t_row)
            limit = t_row + 1
            
            # Contagem de colunas com tempo <= t_row (elas assumem o valor v_row)
            count_base = query(col_time_bit, limit)
            
            best_val = -1
            max_freq = -1
            
            # Iterar de 50 a 0 para garantir que em caso de empate o maior valor é escolhido
            for r in range(MAX_R, -1, -1):
                total = col_total_counts[r]
                if total == 0:
                    # Se não há colunas com valor r, a frequência é 0 (ou count_base se r == v_row)
                    if r == v_row:
                        if count_base > max_freq:
                            max_freq = count_base
                            best_val = r
                    continue
                
                # Contagem de colunas com valor r E tempo > t_row
                # Total com valor r menos as com tempo <= t_row
                le = query(col_val_bits[r], limit)
                late = total - le
                
                current_freq = late
                if r == v_row:
                    current_freq += count_base
                
                if current_freq > max_freq:
                    max_freq = current_freq
                    best_val = r
            
            output_buffer.append(str(best_val))
            
        elif op == 4:
            # Imprimir valor mais frequente na coluna X
            X = int(next(iterator))
            
            t_col = col_time[X]
            v_col = col_val[X]
            
            limit = t_col + 1
            count_base = query(row_time_bit, limit)
            
            best_val = -1
            max_freq = -1
            
            for r in range(MAX_R, -1, -1):
                total = row_total_counts[r]
                if total == 0:
                    if r == v_col:
                        if count_base > max_freq:
                            max_freq = count_base
                            best_val = r
                    continue
                
                le = query(row_val_bits[r], limit)
                late = total - le
                
                current_freq = late
                if r == v_col:
                    current_freq += count_base
                
                if current_freq > max_freq:
                    max_freq = current_freq
                    best_val = r
            
            output_buffer.append(str(best_val))
            
    sys.stdout.write('\n'.join(output_buffer))

if __name__ == '__main__':
    solve()