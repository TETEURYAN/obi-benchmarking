
import sys

def main():
    # Lê todos os números da entrada padrão
    numeros = list(map(int, sys.stdin.read().split()))
    
    # A entrada consiste de 4 números
    a, b, c, d = numeros[0], numeros[1], numeros[2], numeros[3]
    
    # Lógica de identificação:
    # Falsa coral (padrão BVP, período 3): Em qualquer janela de 4 caracteres (BVPB, VPBV, PBVP), 
    # o primeiro e o último caractere são iguais. Logo, a == d.
    # Verdadeira coral (padrão BVBP, período 4): Em qualquer janela de 4 caracteres (BVBP, VBPB, BPBV, PBVB), 
    # o primeiro e o último caractere são diferentes. Logo, a != d.
    
    if a == d:
        print("F")
    else:
        print("V")

if __name__ == "__main__":
    main()
