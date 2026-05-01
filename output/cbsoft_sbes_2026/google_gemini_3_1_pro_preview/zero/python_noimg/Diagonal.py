
import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    N = int(data[0])
    A = [int(x) for x in data[1:N+1]]
    
    events = []
    for b in range(N):
        if A[b] > 0:
            # O prédio b (0-indexado, então prédio b+1) tem apartamentos de 1 até A[b].
            # A diagonal C = a + b_idx (onde b_idx = b + 1 e a vai de 1 até A[b]).
            # Portanto, C varia de (b + 1) + 1 até (b + 1) + A[b].
            # Ou seja, C varia de b + 2 até b + A[b] + 1.
            # Adicionamos um evento de entrada em b + 2 e um de saída em b + A[b] + 2.
            events.append((b + 2, 1))
            events.append((b + A[b] + 2, -1))
            
    # Ordenar os eventos. 
    # Como -1 < 1, eventos de saída (-1) na mesma posição X serão processados 
    # antes dos eventos de entrada (1), o que é correto pois o intervalo termina em X - 1.
    events.sort()
    
    max_overlap = 0
    current_overlap = 0
    
    for pos, val in events:
        if val == 1:
            current_overlap += 1
            if current_overlap > max_overlap:
                max_overlap = current_overlap
        else:
            current_overlap -= 1
            
    print(max_overlap)

if __name__ == '__main__':
    solve()
