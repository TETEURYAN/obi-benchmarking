import sys

sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        A = int(next(iterator))
        N = int(next(iterator))
        M = int(next(iterator))
    except StopIteration:
        return

    rows = []
    for _ in range(N):
        current_row = []
        for _ in range(M):
            val = int(next(iterator))
            current_row.append(val)
        rows.append(current_row)
    
    # O problema diz que as filas são dadas da mais distante para a mais próxima.
    # Ou seja, a primeira fila lida é a fila N, a última é a fila 1.
    # Invertemos a lista para que o índice 0 corresponda à fila 1 (mais próxima do palco).
    rows.reverse()
    
    # Iteramos da fila mais próxima (índice 0) para a mais distante (índice N-1)
    for i in range(N):
        row = rows[i]
        consecutive_zeros = 0
        
        for seat in row:
            if seat == 0:
                consecutive_zeros += 1
                if consecutive_zeros == A:
                    # Encontramos A assentos contíguos.
                    # Como iteramos da mais próxima para a mais distante,
                    # a primeira encontrada é a resposta.
                    # O número da fila é i + 1.
                    print(i + 1)
                    return
            else:
                consecutive_zeros = 0
    
    # Se nenhuma fila satisfaz a condição
    print(-1)

if __name__ == "__main__":
    solve()