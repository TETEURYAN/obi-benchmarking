import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    
    # Fórmula: ((N+1)*(N+2))/2
    # Usamos divisão inteira // para garantir que o resultado seja um inteiro
    resultado = (n + 1) * (n + 2) // 2
    
    print(resultado)

if __name__ == "__main__":
    main()