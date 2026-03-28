import sys

def main():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # Parse dos valores N e F
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        f = int(next(iterator))
    except StopIteration:
        return

    # Leitura dos ciclos
    cycles = []
    for _ in range(n):
        try:
            cycles.append(int(next(iterator)))
        except StopIteration:
            break
            
    # Busca Binária na resposta (Binary Search on Answer)
    # Limites:
    # Mínimo: 0 dias
    # Máximo: Um valor seguro que cubra o pior caso.
    # Restrições: F <= 10^9, C <= 10^6.
    # No pior caso (N=1, C=10^6, F=10^9), precisamos de 10^15 dias.
    # O problema garante resposta <= 10^8, mas usamos um limite superior seguro.
    low = 0
    high = 10**18 
    ans = high
    
    while low <= high:
        mid = (low + high) // 2
        
        # Calcula o total de moedas produzidas em 'mid' dias
        total_coins = 0
        for c in cycles:
            total_coins += mid // c
            # Otimização: se já passamos de F, não precisamos somar o resto
            if total_coins >= f:
                break
        
        # Verificação da condição
        if total_coins >= f:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    print(ans)

if __name__ == '__main__':
    main()