
import sys

def main():
    # Lê toda a entrada de uma vez para facilitar o processamento
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # Cria um iterador para consumir os tokens sequencialmente
    iterator = iter(input_data)
    
    try:
        m = int(next(iterator))
        n = int(next(iterator))
    except StopIteration:
        return

    # Lê os dígitos de X
    x = []
    for _ in range(m):
        x.append(int(next(iterator)))
        
    # Lê os dígitos de Y
    y = []
    for _ in range(n):
        y.append(int(next(iterator)))
    
    # Determina o comprimento máximo para alinhar os números
    max_len = max(m, n)
    
    # Preenche com zeros à direita (menos significativos) para igualar tamanhos
    # Isso alinha os pontos binários implicitamente
    if m < max_len:
        x.extend([0] * (max_len - m))
    if n < max_len:
        y.extend([0] * (max_len - n))
        
    result = []
    carry = 0
    
    # Realiza a adição binária do bit menos significativo (direita) para o mais significativo (esquerda)
    for i in range(max_len - 1, -1, -1):
        bit_sum = x[i] + y[i] + carry
        res_bit = bit_sum % 2
        carry = bit_sum // 2
        result.append(res_bit)
    
    # Como a restrição garante X + Y < 1, não haverá carry final (overflow para o inteiro 1).
    # O resultado está armazenado ao contrário (LSB primeiro), então invertemos.
    result.reverse()
    
    # Remove os zeros à direita (trailing zeros) para satisfazer o formato "obi-2015"
    # O formato exige o menor número de dígitos possível, ou seja, o último dígito deve ser 1.
    while result and result[-1] == 0:
        result.pop()
        
    # Imprime o resultado
    print(*(result))

if __name__ == '__main__':
    main()
