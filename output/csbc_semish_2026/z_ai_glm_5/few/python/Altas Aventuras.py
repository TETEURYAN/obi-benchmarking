import sys

# Aumentar o limite de recursão, embora não seja estritamente necessário para esta solução iterativa.
sys.setrecursionlimit(200000)

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    N = int(input_data[0])
    K = int(input_data[1])

    # Caso especial: se temos apenas 1 balão, devemos testar sequencialmente
    # do 1 até o limite. No pior caso, estoura no último andar ou não estoura,
    # exigindo N testes.
    if K == 1:
        print(N)
        return

    # Para K >= 2, usamos a propriedade da soma de coeficientes binomiais.
    # O número máximo de andares que podemos testar com t testes e k balões
    # é dado por: Soma(C(t, i)) para i de 1 a k.
    # Queremos encontrar o menor t tal que essa soma seja >= N.
    # Como N <= 10^9, t será no máximo cerca de 45000 (para K=2) ou muito menor para K maior.
    
    t = 0
    while True:
        t += 1
        
        # Calculamos a soma dos coeficientes binomiais para o t atual.
        # C(t, i) = C(t, i-1) * (t - i + 1) / i
        
        current_comb = 1 # C(t, 0)
        total_coverage = 0
        
        # O número de termos na soma é limitado por K e por t.
        # Se K > t, a soma é completa (2^t - 1), mas t será pequeno nesse caso.
        limit = min(K, t)
        
        for i in range(1, limit + 1):
            # Atualiza o coeficiente binomial iterativamente
            current_comb = current_comb * (t - i + 1) // i
            total_coverage += current_comb
            
            # Se a cobertura já excede N, podemos parar de somar
            if total_coverage >= N:
                break
        
        if total_coverage >= N:
            print(t)
            return

if __name__ == '__main__':
    solve()