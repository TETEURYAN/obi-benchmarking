import sys

sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    L = int(input_data[0])
    
    # O problema pede para dividir a barra em 4 pedaços sucessivamente
    # enquanto o lado for maior ou igual a 2.
    # Isso é equivalente a contar quantas vezes podemos dividir L por 2
    # até que o resultado seja menor que 2 (ou seja, igual a 1, pois L é inteiro).
    # Seja k o número de divisões. O número total de pedaços será 4^k.
    # k é equivalente a floor(log2(L)).
    # Em Python, L.bit_length() retorna floor(log2(L)) + 1.
    
    k = L.bit_length() - 1
    
    # O resultado é 4^k, que pode ser calculado como 2^(2k) usando bit shift.
    result = 1 << (2 * k)
    
    print(result)

if __name__ == '__main__':
    solve()