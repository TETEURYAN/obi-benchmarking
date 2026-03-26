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
        N = int(next(iterator))
        K = int(next(iterator))
    except StopIteration:
        return

    primes = []
    for _ in range(K):
        try:
            primes.append(int(next(iterator)))
        except StopIteration:
            break
    
    # Ordenar os primos é crucial para a lógica de Crivo Combinatório
    primes.sort()
    
    # Abordagem: Crivo Combinatório (Combinatorial Sieve)
    # Complexidade: O(K * sqrt(N))
    # Isso é muito mais eficiente que Inclusion-Exclusion O(2^K) quando K é grande (até 40).
    
    # Identificar todos os valores distintos de floor(N/i) para 1 <= i <= N.
    # Existem aproximadamente 2*sqrt(N) valores distintos.
    # Estes formam os estados da nossa DP.
    limit = int(N**0.5)
    
    values_set = set()
    for i in range(1, limit + 1):
        values_set.add(N // i)
        values_set.add(i)
    
    # Ordenar os valores em ordem decrescente.
    # Isso é necessário para a atualização da DP: ao processar um valor v,
    # dependemos do valor v // p, que é estritamente menor que v.
    # Processar em ordem decrescente garante que usamos os valores do "estado anterior".
    values = sorted(list(values_set), reverse=True)
    
    # Inicialização da DP
    # dp[v] armazena a contagem de números <= v que não são divisíveis por nenhum primo processado até agora.
    # Inicialmente, sem processar nenhum primo, todos os números são válidos, logo dp[v] = v.
    dp = {v: v for v in values}
    
    # Processar cada primo p da lista
    for p in primes:
        # Para cada valor v que precisamos calcular
        for v in values:
            # Se v < p, então v // p é 0, e não há múltiplos de p a subtrair.
            # Como values está ordenado decrescentemente, podemos parar o loop interno.
            if v < p:
                break
            
            # A fórmula de atualização:
            # A contagem de números não divisíveis pelos primos processados até agora (incluindo p)
            # é igual a contagem anterior (sem considerar p) menos a contagem de múltiplos de p.
            # Os múltiplos de p são p*1, p*2, ..., p*(v//p).
            # A contagem de múltiplos de p que não são divisíveis pelos primos anteriores é dp[v // p].
            dp[v] -= dp[v // p]
            
    # A resposta para N é o valor calculado para o estado N.
    print(dp[N])

if __name__ == '__main__':
    solve()