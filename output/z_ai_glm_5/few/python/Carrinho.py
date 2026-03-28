import sys

def solve():
    # Leitura rápida de todos os dados de entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        # Lendo N e D
        n_batteries = int(next(iterator))
        d_total = float(next(iterator))
    except StopIteration:
        return

    batteries = []
    for _ in range(n_batteries):
        p = float(next(iterator))
        c = float(next(iterator))
        batteries.append((p, c))
    
    # Adicionamos o ponto de chegada (D) como um "nó final"
    # A carga não importa aqui, pois não saímos deste ponto.
    batteries.append((d_total, 0.0))
    
    # Número de nós (baterias + chegada)
    m = n_batteries + 1
    
    # dp[i] = tempo mínimo para chegar à bateria i
    # Inicializamos com infinito, exceto a posição inicial
    dp = [float('inf')] * m
    dp[0] = 0.0
    
    # Iteramos sobre cada bateria de destino k
    for k in range(1, m):
        pk, _ = batteries[k]
        
        # Verificamos todas as baterias anteriores i de onde poderíamos ter vindo
        # A complexidade é O(N^2), que para N=1000 é perfeitamente aceitável (1.000.000 operações)
        for i in range(k):
            pi, ci = batteries[i]
            
            # Se não conseguimos chegar em i, não podemos partir de i
            if dp[i] == float('inf'):
                continue
            
            # Distância do segmento
            dist = pk - pi
            
            # Tempo gasto neste segmento: (dist)^2 / Carga
            # Fórmula derivada de: tempo = dist/V, V_max = C/dist
            time_segment = (dist * dist) / ci
            
            # Relaxamento
            if dp[i] + time_segment < dp[k]:
                dp[k] = dp[i] + time_segment

    # Imprimimos o resultado para o último nó (chegada)
    # Formato com exatamente 3 casas decimais
    print("{:.3f}".format(dp[m-1]))

if __name__ == '__main__':
    solve()