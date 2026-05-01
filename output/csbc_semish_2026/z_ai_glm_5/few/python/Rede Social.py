import sys

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # O primeiro elemento é N
    n = int(input_data[0])
    
    # Os elementos restantes são os índices de repostagem
    # Convertemos para inteiros
    reposts = list(map(int, input_data[1:]))
    
    # Ordenamos os índices em ordem crescente
    reposts.sort()
    
    ans = 0
    
    # Lógica: Queremos encontrar o maior k tal que existam k mensagens com índice >= k.
    # Se ordenarmos a lista de índices R em ordem crescente:
    # R[0] <= R[1] <= ... <= R[n-1]
    # Para um dado k, precisamos que o k-ésimo maior elemento seja >= k.
    # O k-ésimo maior elemento é o elemento de índice (n - k) na lista ordenada (0-indexado).
    # Portanto, a condição é: R[n - k] >= k.
    # Como R é crescente, R[n-k] é o menor valor entre os k maiores elementos.
    # Se R[n-k] >= k, então todos os k elementos a partir de n-k são >= k.
    # 
    # Iteramos k de n até 1. O primeiro k que satisfizer a condição é a resposta.
    # Podemos otimizar iterando i de 0 até n-1 (onde i = n - k).
    # Condição: R[i] >= n - i.
    # O primeiro i que satisfaz isso nos dá o maior k = n - i.
    
    for i in range(n):
        if reposts[i] >= n - i:
            ans = n - i
            break
            
    print(ans)

if __name__ == '__main__':
    solve()