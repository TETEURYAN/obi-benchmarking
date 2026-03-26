import sys
import heapq

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        N = int(next(iterator))
        K = int(next(iterator))
    except StopIteration:
        return

    # Coletar posições dos amigos no lado superior
    top_positions = []
    # O problema diz que as posições são 1 a N. Vamos manter 1-based.
    for i in range(1, N + 1):
        try:
            val = int(next(iterator))
            if val == 1:
                top_positions.append(i)
        except StopIteration:
            break
            
    # Coletar posições dos amigos no lado inferior
    bot_positions = []
    for i in range(1, N + 1):
        try:
            val = int(next(iterator))
            if val == 1:
                bot_positions.append(i)
        except StopIteration:
            break

    # Como iteramos de 1 a N, as posições já estão ordenadas.
    # O problema garante que existem exatamente K amigos em cada lado.

    total_swaps = 0
    # Max-heap para armazenar os limites inferiores (L') transformados.
    # Python heapq é min-heap, então armazenamos valores negativos.
    max_heap = []

    for k in range(K):
        t_pos = top_positions[k]
        b_pos = bot_positions[k]

        # Custo base para o par k se alinhar, ignorando restrições de ordem
        # Corresponde a |t_pos - b_pos|
        L = min(t_pos, b_pos)
        R = max(t_pos, b_pos)
        
        total_swaps += (R - L)

        # Transformação para garantir p_k < p_{k+1}
        # Seja q_k = p_k - k. A restrição p_k < p_{k+1} torna-se q_k <= q_{k+1}.
        # O intervalo viável para q_k é [L - k, R - k].
        L_prime = L - k
        R_prime = R - k

        # Adiciona o limite inferior transformado ao heap
        heapq.heappush(max_heap, -L_prime)

        # Verifica se o maior limite inferior excede o limite superior atual
        # -max_heap[0] é o valor máximo de L' no heap atual
        current_max_L = -max_heap[0]

        if current_max_L > R_prime:
            # Há conflito. Precisamos ajustar a posição ótima para baixo (para o valor R_prime)
            # ou ajustar valores anteriores para cima.
            # A lógica do heap garante que isso minimiza a soma das distâncias.
            
            # O custo adicional é a distância movida vezes 2.
            # (Porque mover p afeta |a-p| + |b-p|, e a derivada é 2 fora do intervalo [L, R])
            total_swaps += 2 * (current_max_L - R_prime)
            
            # Removemos o limite inferior problemático e inserimos R_prime.
            # Isso simula que o grupo de intervalos representado por esse heap
            # agora está "travado" ou "ancorado" em R_prime.
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, -R_prime)

    print(total_swaps)

if __name__ == '__main__':
    solve()