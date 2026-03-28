import sys

# Aumentar o limite de recursão, embora a solução seja iterativa.
sys.setrecursionlimit(300000)

def main():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # Iterador para processar os tokens de entrada sequencialmente
    iterator = iter(input_data)
    
    try:
        n_str = next(iterator)
        N = int(n_str)
    except StopIteration:
        return

    # Leitura das posições X
    X = [0] * N
    for i in range(N):
        X[i] = int(next(iterator))
        
    # Leitura das alturas H
    H = [0] * N
    for i in range(N):
        H[i] = int(next(iterator))
        
    # Arrayss para Programação Dinâmica
    # reach[i]: a posição mais distante alcançada pela cadeia iniciada em i
    # cnt[i]: quantidade de dominós derrubados pela cadeia iniciada em i
    # nxt[i]: índice do primeiro dominó que NÃO cai quando a cadeia de i é disparada
    reach = [0] * N
    cnt = [0] * N
    nxt = [0] * N
    
    # Processamos os dominós da direita para a esquerda
    for i in range(N - 1, -1, -1):
        # O dominó i cai e alcança inicialmente até X[i] + H[i]
        curr_reach = X[i] + H[i]
        curr_cnt = 1
        j = i + 1
        
        # Enquanto houver dominós à direita (j < N) e o início do próximo dominó (X[j])
        # estiver dentro do alcance atual da cadeia (curr_reach)
        while j < N and X[j] <= curr_reach:
            # A cadeia de i engloba a cadeia de j.
            # O alcance se expande para o máximo entre o atual e o alcance de j.
            if reach[j] > curr_reach:
                curr_reach = reach[j]
            
            # Contamos todos os dominós que cairam na cadeia de j
            curr_cnt += cnt[j]
            
            # Avançamos para o primeiro dominó que não caiu na cadeia de j.
            # Como processamos da direita para esquerda, nxt[j] já foi calculado.
            j = nxt[j]
        
        # Armazenamos os resultados para i
        reach[i] = curr_reach
        cnt[i] = curr_cnt
        nxt[i] = j
        
    # Imprimir o resultado
    # Usar join e map(str, ...) é eficiente e evita problemas com print(*list) para N grande
    sys.stdout.write(' '.join(map(str, cnt)) + '\n')

if __name__ == '__main__':
    main()