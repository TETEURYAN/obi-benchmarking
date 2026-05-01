import sys

# Aumentar o limite de recursão, embora a solução seja iterativa
sys.setrecursionlimit(200000)

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # conflict_mask[i] é uma bitmaska onde o bit j está setado se os ingredientes i e j não combinam.
    # Isso permite verificar conflitos em O(1) para cada ingrediente presente no sanduíche.
    conflict_mask = [0] * n

    for _ in range(m):
        try:
            u = int(next(iterator)) - 1
            v = int(next(iterator)) - 1
        except StopIteration:
            break
        
        # Marca o ingrediente v como conflitante com u e vice-versa
        conflict_mask[u] |= (1 << v)
        conflict_mask[v] |= (1 << u)

    count = 0
    
    # Itera por todos os subconjuntos possíveis (máscaras de bits).
    # O intervalo é [1, 2^n - 1] pois o sanduíche deve conter ao menos um ingrediente.
    # N <= 20, então 2^20 é aproximadamente 10^6, o que é viável.
    for mask in range(1, 1 << n):
        is_valid = True
        
        # Verifica se o subconjunto atual contém algum par proibido
        for i in range(n):
            # Se o ingrediente 'i' está no sanduíche (bit i está setado na máscara)
            if (mask >> i) & 1:
                # Verifica se existe algum ingrediente conflitante também no sanduíche.
                # mask & conflict_mask[i] será diferente de 0 se houver conflito.
                if (mask & conflict_mask[i]):
                    is_valid = False
                    break
        
        if is_valid:
            count += 1
            
    print(count)

if __name__ == "__main__":
    solve()