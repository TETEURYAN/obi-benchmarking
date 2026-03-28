import sys

# Aumentar o limite de recursão para evitar erros com a estrutura DSU
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

    # Estrutura DSU (Union-Find)
    # parent[i] aponta para o representante do conjunto.
    # Inicialmente, cada vaga i aponta para si mesma.
    # A vaga 0 é usada como sentinela para indicar "nenhuma vaga disponível".
    parent = list(range(n + 1))

    def find(i):
        # Path compression: otimização para que futuras buscas sejam O(1)
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]

    count = 0
    
    # Processar cada cliente
    for _ in range(m):
        try:
            v = int(next(iterator))
        except StopIteration:
            break
            
        # Encontrar a maior vaga disponível que seja <= v
        spot = find(v)
        
        # Se spot for 0, significa que não há vagas disponíveis no intervalo [1, v]
        # Conforme o problema, o estacionamento para de aceitar carros.
        if spot == 0:
            break
        
        # Ocupar a vaga 'spot'.
        # Union: ligamos a vaga 'spot' à vaga anterior 'spot - 1'.
        # Assim, se alguém procurar 'spot' novamente, será redirecionado para 'spot - 1'.
        parent[spot] = find(spot - 1)
        count += 1

    print(count)

if __name__ == '__main__':
    solve()