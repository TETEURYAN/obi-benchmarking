
import sys

def main():
    data = sys.stdin.read().strip().split()
    if len(data) != 4:
        return
    a, b, c, d = map(int, data)
    
    # Padrão verdadeiro: ...BVBPBVBPBVBP... (repetição de 4 cores)
    # Para 4 números consecutivos: posições 1 e 4 iguais, posições 2 e 3 diferentes entre si e diferentes de 1/4
    # Padrão falso: ...BVPBVPBVPBVP... (repetição de 3 cores)
    # Para 4 números consecutivos: posições 1 e 4 diferentes
    
    if a == d and b != c and a != b and a != c:
        print("V")
    else:
        print("F")

if __name__ == "__main__":
    main()
