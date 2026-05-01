import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    N = int(data[0])
    D = int(data[1])
    A = int(data[2])
    
    # Calcula a diferença diretamente
    diff = D - A
    # Se diff > 0, já está na posição correta, apertar 0 vezes
    # Se diff < 0, precisa apertar N - (abs(diff)) vezes para avançar
    if diff >= 0:
        result = 0
    else:
        result = N - abs(diff)
    
    print(result)

if __name__ == "__main__":
    main()