
import sys

def main():
    # Lê todas as entradas de uma vez
    data = sys.stdin.read().split()
    
    if not data:
        return

    # Converte para inteiros
    A = int(data[0])
    B = int(data[1])
    C = int(data[2])
    D = int(data[3])

    # Verifica as três condições
    # 1. A = B + C + D
    # 2. B + C = D
    # 3. B = C
    if (A == B + C + D) and (B + C == D) and (B == C):
        print("S")
    else:
        print("N")

if __name__ == "__main__":
    main()
