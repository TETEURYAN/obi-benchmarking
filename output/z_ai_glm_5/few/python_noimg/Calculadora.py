import sys
import math

# Otimização para leitura de entrada e limite de recursão
sys.setrecursionlimit(200000)

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    n = int(input_data[0])
    
    # O visor inicia com 1. Representamos como uma fração numerador/denominador
    numerator = 1
    denominator = 1
    
    # Os dados começam no índice 1. Cada operação ocupa 2 tokens (dígito, operador).
    # Portanto, os pares estão em input_data[1], input_data[2], depois input_data[3], input_data[4], etc.
    # Para a i-ésima operação (0-indexada):
    # Dígito está em input_data[1 + 2*i]
    # Operador está em input_data[1 + 2*i + 1]
    
    for i in range(n):
        digit = int(input_data[1 + 2 * i])
        operator = input_data[2 + 2 * i]
        
        if operator == '*':
            numerator *= digit
        else: # operator == '/'
            denominator *= digit
            
        # Otimização crucial: Simplificar a fração a cada passo.
        # Isso mantém os números pequenos, evitando que explodam para inteiros gigantes
        # que poderiam tornar a multiplicação lenta, mesmo em Python.
        # Como os números são compostos por fatores primos pequenos (dígitos 1-9),
        # o custo do GCD é baixo.
        common_divisor = math.gcd(numerator, denominator)
        numerator //= common_divisor
        denominator //= common_divisor
        
    # O problema garante que o resultado final é um inteiro, logo denominator será 1.
    print(numerator)

if __name__ == '__main__':
    solve()