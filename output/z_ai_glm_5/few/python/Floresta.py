
import sys

def solve():
    # Leitura rápida da entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    N = int(input_data[0])
    
    # A equação derivada para o total de árvores N é:
    # N = 2xy - x - y + 1
    # Manipulando para encontrar os fatores:
    # 2N - 1 = (2x - 1)(2y - 1)
    # Precisamos encontrar o número de pares (x, y) tal que x >= 2 e y >= 2.
    # Isso implica que os fatores (2x - 1) >= 3 e (2y - 1) >= 3.
    
    K = 2 * N - 1
    count = 0
    
    # O valor máximo para o divisor d é a raiz quadrada de K.
    # Como K <= 2*10^9, a raiz é aproximadamente 45000, o que é muito rápido.
    limit = int(K**0.5)
    
    # Iteramos os divisores d. Como d <= K/d, se d >= 3, então K/d >= d >= 3.
    # Então, basta contar os divisores d onde d >= 3 e d <= sqrt(K).
    # O loop começa de 3 para satisfazer a condição d >= 3.
    for d in range(3, limit + 1):
        if K % d == 0:
            count += 1
            
    print(count)

if __name__ == '__main__':
    solve()
