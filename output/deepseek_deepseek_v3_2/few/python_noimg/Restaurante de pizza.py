import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    A, B, R, G = map(int, data)
    
    # Restrição 1: a pizza (círculo de raio R) deve caber na caixa retangular A x B
    # Isso significa que o diâmetro (2*R) deve ser <= min(A, B)
    if 2 * R > min(A, B):
        print("N")
        return
    
    # Restrição 2: o ângulo G deve dividir 360° igualmente
    # Ou seja, 360 deve ser múltiplo de G
    if 360 % G != 0:
        print("N")
        return
    
    print("S")

if __name__ == "__main__":
    main()