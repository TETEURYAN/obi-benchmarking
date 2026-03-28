import sys
import heapq

def main():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        C = int(next(iterator))
        N = int(next(iterator))
    except StopIteration:
        return

    # Min-heap para armazenar o momento em que cada caixa ficará livre.
    # Inicialmente, todos os C caixas estão livres no tempo 0.
    tellers = [0] * C
    heapq.heapify(tellers)

    late_clients = 0

    for _ in range(N):
        try:
            T = int(next(iterator))
            D = int(next(iterator))
        except StopIteration:
            break

        # Pega o caixa que ficará livre mais cedo
        free_time = heapq.heappop(tellers)

        # O atendimento começa no máximo entre o tempo de chegada e o tempo de liberação do caixa
        start_time = max(T, free_time)

        # Verifica se o tempo de espera excede 20 minutos
        if start_time - T > 20:
            late_clients += 1

        # O caixa ficará ocupado por D minutos após o início do atendimento
        heapq.heappush(tellers, start_time + D)

    print(late_clients)

if __name__ == "__main__":
    main()