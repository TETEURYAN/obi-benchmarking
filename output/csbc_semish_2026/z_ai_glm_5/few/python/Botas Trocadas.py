import sys

def solve():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    n = int(input_data[0])
    
    # Tamanhos M estão entre 30 e 60.
    # Criamos listas de contagem para o pé esquerdo (E) e direito (D).
    # O índice do vetor representa o tamanho da bota.
    count_esquerdo = [0] * 61
    count_direito = [0] * 61
    
    # Os dados começam após o primeiro número (N).
    # O formato é M L, então lemos em pares.
    idx = 1
    for _ in range(n):
        tamanho = int(input_data[idx])
        pe = input_data[idx + 1]
        
        if pe == 'E':
            count_esquerdo[tamanho] += 1
        else:
            count_direito[tamanho] += 1
            
        idx += 2
        
    total_pares = 0
    # Iteramos sobre todos os tamanhos possíveis para formar pares.
    # Um par requer uma bota esquerda e uma direita do mesmo tamanho.
    for tamanho in range(30, 61):
        total_pares += min(count_esquerdo[tamanho], count_direito[tamanho])
        
    print(total_pares)

if __name__ == '__main__':
    solve()