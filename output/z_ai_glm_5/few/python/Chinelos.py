import sys

def solve():
    # Lê toda a entrada de uma vez para eficiência
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # Cria um iterador para processar os tokens sequencialmente
    iterator = iter(input_data)
    
    try:
        # Lê o número de tamanhos (N)
        n = int(next(iterator))
    except StopIteration:
        return

    # Inicializa o vetor de estoque.
    # Usamos índice de 1 a N para corresponder diretamente aos tamanhos.
    # O índice 0 é ignorado.
    stock = [0] * (n + 1)
    
    for i in range(1, n + 1):
        try:
            stock[i] = int(next(iterator))
        except StopIteration:
            break
            
    try:
        # Lê o número de pedidos (P)
        p = int(next(iterator))
    except StopIteration:
        # Se não houver pedidos, a resposta é 0
        print(0)
        return

    sold_count = 0
    
    # Processa cada pedido
    for _ in range(p):
        try:
            size = int(next(iterator))
            # Verifica se o tamanho é válido e se há estoque
            if 1 <= size <= n and stock[size] > 0:
                stock[size] -= 1
                sold_count += 1
        except StopIteration:
            break
            
    print(sold_count)

if __name__ == "__main__":
    solve()