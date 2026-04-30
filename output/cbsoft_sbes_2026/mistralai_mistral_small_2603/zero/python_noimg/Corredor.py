
import sys

def main():
    N = int(sys.stdin.readline())
    vidas = list(map(int, sys.stdin.readline().split()))
    
    max_vidas = -float('inf')
    soma_atual = 0
    min_soma = 0
    
    for vida in vidas:
        soma_atual += vida
        if soma_atual - min_soma > max_vidas:
            max_vidas = soma_atual - min_soma
        if soma_atual < min_soma:
            min_soma = soma_atual
    
    print(max_vidas)

if __name__ == "__main__":
    main()
