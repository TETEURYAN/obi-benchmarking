
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    m = int(data[0])
    n = int(data[1])
    
    x_digits = list(map(int, data[2:2+m]))
    y_digits = list(map(int, data[2+m:2+m+n]))
    
    # Calcular o valor decimal de X e Y
    x_val = 0.0
    for i, digit in enumerate(x_digits):
        if digit == 1:
            x_val += 1 / (2 ** (i + 1))
    
    y_val = 0.0
    for j, digit in enumerate(y_digits):
        if digit == 1:
            y_val += 1 / (2 ** (j + 1))
    
    total = x_val + y_val
    
    # Converter para representação obi-2015
    # Encontrar o menor número de dígitos necessário
    # Como X + Y < 1, não precisamos de parte inteira
    
    # Representação binária fracionária: multiplicar por 2 repetidamente
    # Para garantir precisão, vamos usar frações racionais
    # Representar total como fração
    
    # Como os valores são somas de potências de 1/2, o resultado é um número racional com denominador potência de 2
    # Vamos calcular diretamente a representação binária
    
    # Encontrar o denominador comum: 2^max_len onde max_len é suficientemente grande
    # Como M, N <= 1000, o resultado pode ter até 1001 dígitos (no pior caso)
    # Vamos usar até 2000 dígitos para garantir
    
    # Mas podemos ser mais inteligentes: calcular a representação diretamente
    # Usando frações exatas
    
    from fractions import Fraction
    
    # Calcular X e Y como frações
    x_frac = Fraction(0, 1)
    for i, digit in enumerate(x_digits):
        if digit == 1:
            x_frac += Fraction(1, 2**(i+1))
    
    y_frac = Fraction(0, 1)
    for j, digit in enumerate(y_digits):
        if digit == 1:
            y_frac += Fraction(1, 2**(j+1))
    
    total_frac = x_frac + y_frac
    
    # Converter para representação binária
    # total_frac é uma fração entre 0 e 1
    # Representação: d1 d2 d3 ... onde di = 1 se (2^i * total_frac) tem parte inteira ímpar após subtrair os dígitos anteriores
    
    # Algoritmo: multiplicar por 2, pegar parte inteira como dígito, continuar com a parte fracionária
    result = []
    frac = total_frac
    
    # Encontrar o menor número de dígitos necessário (garantindo que o último dígito seja 1)
    # Continuar até que a fração seja zero ou até termos representação exata
    # Como X+Y < 1, não precisamos de parte inteira
    
    # O número de dígitos necessários é o denominador da fração reduzida (potência de 2)
    # Vamos calcular até que a fração seja zero
    
    # Mas precisamos garantir que o último dígito seja 1 (menor representação possível)
    # Então vamos calcular até que a fração seja zero, e depois remover zeros à direita
    
    while frac > 0:
        frac *= 2
        if frac >= 1:
            result.append(1)
            frac -= 1
        else:
            result.append(0)
    
    # Remover zeros à direita (garantir que o último dígito seja 1)
    while result and result[-1] == 0:
        result.pop()
    
    # Se o resultado estiver vazio (caso total == 0, mas o problema diz X, Y > 0, então isso não deve acontecer)
    if not result:
        result = [0]
    
    # Converter para string e imprimir
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
