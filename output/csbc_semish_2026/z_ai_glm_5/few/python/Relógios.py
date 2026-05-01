import sys
import heapq

# Aumentar o limite de recursao, embora seja uma solucao iterativa
sys.setrecursionlimit(200000)

def solve():
    # Leitura rapida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        L = int(next(iterator))
        C = int(next(iterator))
        K = int(next(iterator))
    except StopIteration:
        return

    # Leitura da grade
    grid = []
    for _ in range(L):
        row = []
        for _ in range(C):
            row.append(int(next(iterator)))
        grid.append(row)

    # Dijkstra
    # dist[r][c] armazena o tempo minimo para alcancar (r, c)
    dist = [[float('inf')] * C for _ in range(L)]
    dist[0][0] = 0
    
    # Fila de prioridade: (tempo, linha, coluna)
    pq = [(0, 0, 0)]
    
    # Movimentos: direita, esquerda, baixo, cima
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    
    while pq:
        t, r, c = heapq.heappop(pq)
        
        # Se ja encontramos um caminho melhor para (r, c), ignoramos
        if t > dist[r][c]:
            continue
        
        # Se chegamos ao destino, o tempo minimo garantido pelo Dijkstra eh a resposta
        if r == L - 1 and c == C - 1:
            print(t)
            return

        current_val = grid[r][c]
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            
            if 0 <= nr < L and 0 <= nc < C:
                neighbor_val = grid[nr][nc]
                
                # Caso 1: Relogio atual PARADO (current_val >= 0)
                # Nao podemos esperar. Devemos mover imediatamente em t + 1.
                if current_val != -1:
                    t_next = t + 1
                    
                    if neighbor_val == -1:
                        # Vizinho funcionando: sempre aceita
                        if t_next < dist[nr][nc]:
                            dist[nr][nc] = t_next
                            heapq.heappush(pq, (t_next, nr, nc))
                    else:
                        # Vizinho parado: verifica se o tempo coincide
                        if t_next % K == neighbor_val:
                            if t_next < dist[nr][nc]:
                                dist[nr][nc] = t_next
                                heapq.heappush(pq, (t_next, nr, nc))
                
                # Caso 2: Relogio atual FUNCIONANDO (current_val == -1)
                # Podemos esperar. Queremos mover para o vizinho no menor tempo valido.
                else:
                    if neighbor_val == -1:
                        # Vizinho funcionando: mover em t + 1
                        t_next = t + 1
                        if t_next < dist[nr][nc]:
                            dist[nr][nc] = t_next
                            heapq.heappush(pq, (t_next, nr, nc))
                    else:
                        # Vizinho parado em P.
                        # Precisamos de um tempo T >= t + 1 tal que T % K == P.
                        t_min = t + 1
                        rem = t_min % K
                        P_next = neighbor_val
                        
                        if rem == P_next:
                            t_arr = t_min
                        else:
                            # Calcula o tempo de espera necessario
                            wait = (P_next - rem + K) % K
                            t_arr = t_min + wait
                        
                        if t_arr < dist[nr][nc]:
                            dist[nr][nc] = t_arr
                            heapq.heappush(pq, (t_arr, nr, nc))

    # Se a fila esvaziar sem chegar ao destino
    print(-1)

if __name__ == '__main__':
    solve()