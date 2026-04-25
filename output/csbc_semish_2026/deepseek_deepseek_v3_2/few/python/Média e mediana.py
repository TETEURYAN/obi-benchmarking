import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    A, B = map(int, data)
    # Para média = mediana, o terceiro número deve ser tal que:
    # Ao ordenar os três números, o número mediano seja igual ao valor da média.
    # Se A < B, então C pode ser menor que A, entre A e B, ou maior que B.
    # A mediana será:
    #   - A, se C <= A
    #   - C, se A < C < B
    #   - B, se C >= B
    # A média é (A+B+C)/3
    # Para ser igual à mediana:
    
    # Caso 1: Mediana = A -> C <= A
    # Equação: (A+B+C)/3 = A -> A+B+C = 3A -> C = 2A - B
    # Verificamos se C <= A (garantindo mediana A)
    C1 = 2*A - B
    if C1 <= A:
        print(C1)
        return
    
    # Caso 2: Mediana = C -> A < C < B
    # Equação: (A+B+C)/3 = C -> A+B+C = 3C -> A+B = 2C -> C = (A+B)/2
    # Verificamos se C é inteiro e se A < C < B
    soma = A + B
    if soma % 2 == 0:
        C2 = soma // 2
        if A < C2 < B:
            print(C2)
            return
    
    # Caso 3: Mediana = B -> C >= B
    # Equação: (A+B+C)/3 = B -> A+B+C = 3B -> C = 2B - A
    # Verificamos se C >= B (garantindo mediana B)
    C3 = 2*B - A
    if C3 >= B:
        print(C3)
        return
    
    # Se nenhum caso fornece solução válida (inexistente no problema, mas fallback)
    # O problema sempre tem solução, então não deveria ocorrer.
    # Escolhemos o menor dos candidatos que satisfaz a igualdade média=mediana.
    # Na prática, C1 será sempre o menor possível.
    print(C1)

if __name__ == "__main__":
    main()