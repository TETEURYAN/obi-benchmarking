import sys

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # Conversão para inteiros
    nums = list(map(int, input_data))
    
    m = nums[0]
    n = nums[1]
    
    # Extraindo os vetores X e Y
    # X começa no índice 2 e tem tamanho M
    x = nums[2 : 2 + m]
    # Y começa no índice 2+M e tem tamanho N
    y = nums[2 + m : 2 + m + n]
    
    # Determinando o tamanho máximo para alinhamento
    max_len = max(m, n)
    
    # Preenchendo o menor vetor com zeros à direita
    # Isso equivale a adicionar 0 * 2^-k, não alterando o valor
    if m < max_len:
        x.extend([0] * (max_len - m))
    elif n < max_len:
        y.extend([0] * (max_len - n))
    
    # Vetor para o resultado
    res = [0] * max_len
    carry = 0
    
    # Adição binária da direita para esquerda (menos significativo para mais)
    for i in range(max_len - 1, -1, -1):
        total = x[i] + y[i] + carry
        res[i] = total % 2
        carry = total // 2
        
    # A restrição X + Y < 1 garante que não há carry final
    
    # Remover zeros à direita para obter a representação mínima
    while res and res[-1] == 0:
        res.pop()
        
    # Imprimir resultado
    print(*res)

if __name__ == '__main__':
    solve()