import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    row = list(map(int, data[1:1 + n]))
    
    # Redução iterativa usando propriedade de combinação modular
    # A cor final é o produto das cores iniciais ponderado pelo coeficiente binomial C(n-1, i) módulo 2
    # Pois a regra é equivalente a XOR (1 = preta, -1 = branca) e a propagação segue o triângulo de Pascal mod 2
    # Última bola = produto de row[i]^(C(n-1, i) mod 2)
    # Como -1 ≡ 1 (mod 2) para expoente par, e -1 ≡ -1 (mod 2) para expoente ímpar,
    # basta contar quantos C(n-1, i) são ímpares com row[i] == -1.
    # C(n-1, i) é ímpar sse (n-1 & i) == i (teorema de Lucas).
    # Então resultado = (-1)^(popcount de (n-1 & i) para i onde row[i] == -1)
    
    n_minus_1 = n - 1
    parity = 0
    for i in range(n):
        if row[i] == -1:
            # Verifica se C(n-1, i) é ímpar
            if (n_minus_1 & i) == i:
                parity ^= 1
    
    if parity == 0:
        print("preta")
    else:
        print("branca")

if __name__ == "__main__":
    main()