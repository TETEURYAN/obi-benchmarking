import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    N = int(data[0])
    G = int(data[1])
    M = int(data[2])
    
    total_pedacos = G * 8 + M * 6
    pedacos_distribuidos = min(N, total_pedacos)
    sobra = total_pedacos - pedacos_distribuidos
    print(sobra)

if __name__ == "__main__":
    main()