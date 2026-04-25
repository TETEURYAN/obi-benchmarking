import sys
sys.setrecursionlimit(200000)

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    Q = int(next(it))
    
    # R vai de 0 a 50
    MAX_VAL = 50
    
    # Para cada linha/coluna, armazenamos:
    # - O valor atual atribuído (ou None se não houver atribuição recente)
    # - O timestamp da última atribuição
    # - Um contador de frequências dos valores que aparecem na linha/coluna
    #   (considerando sobreposições de operações)
    
    # Inicialização
    row_val = [0] * (N + 1)
    row_time = [-1] * (N + 1)
    col_val = [0] * (N + 1)
    col_time = [-1] * (N + 1)
    
    # Para cada valor (0..50), armazenamos quantas linhas/colunas têm esse valor como atribuição atual
    row_count = [0] * (MAX_VAL + 1)
    col_count = [0] * (MAX_VAL + 1)
    
    # Timestamp global
    timestamp = 0
    
    out_lines = []
    
    for _ in range(Q):
        op = int(next(it))
        if op == 1:
            X = int(next(it))
            R = int(next(it))
            # Atualizar contador do valor antigo
            old_val = row_val[X]
            row_count[old_val] -= 1
            # Atribuir novo valor
            row_val[X] = R
            row_time[X] = timestamp
            row_count[R] += 1
            timestamp += 1
        elif op == 2:
            X = int(next(it))
            R = int(next(it))
            old_val = col_val[X]
            col_count[old_val] -= 1
            col_val[X] = R
            col_time[X] = timestamp
            col_count[R] += 1
            timestamp += 1
        elif op == 3:
            X = int(next(it))
            # Valor base da linha
            base_val = row_val[X]
            base_time = row_time[X]
            # Contar frequências
            freq = [0] * (MAX_VAL + 1)
            # Todas as colunas contribuem
            # Se a coluna foi atribuída depois da linha, prevalece o valor da coluna
            # Senão, prevalece o valor da linha
            for c in range(1, N + 1):
                if col_time[c] > base_time:
                    val = col_val[c]
                else:
                    val = base_val
                freq[val] += 1
            # Encontrar valor mais frequente, maior em caso de empate
            best_val = 0
            best_freq = 0
            for v in range(MAX_VAL + 1):
                if freq[v] > best_freq or (freq[v] == best_freq and v > best_val):
                    best_freq = freq[v]
                    best_val = v
            out_lines.append(str(best_val))
        else:  # op == 4
            X = int(next(it))
            base_val = col_val[X]
            base_time = col_time[X]
            freq = [0] * (MAX_VAL + 1)
            for r in range(1, N + 1):
                if row_time[r] > base_time:
                    val = row_val[r]
                else:
                    val = base_val
                freq[val] += 1
            best_val = 0
            best_freq = 0
            for v in range(MAX_VAL + 1):
                if freq[v] > best_freq or (freq[v] == best_freq and v > best_val):
                    best_freq = freq[v]
                    best_val = v
            out_lines.append(str(best_val))
    
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()