import sys
import itertools

def solve():
    # Leitura rápida da entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    N = int(input_data[0])
    M = int(input_data[1])
    
    # Requisitos:
    # 1. Total de palavras T: N <= T <= M
    # 2. Palavras distintas D: D >= M/2
    #
    # Estratégia:
    # Se gerarmos K palavras distintas, onde K = max(N, M//2), satisfazemos ambas as condições.
    # - Se K = N, então N >= M/2 (pois max escolheu N). Temos N palavras distintas. Total N. OK.
    # - Se K = M/2, então M/2 > N (ou >=). Temos M/2 palavras distintas. Total M/2. 
    #   Como M/2 >= N (neste caso) e M/2 <= M, o total está dentro dos limites.
    
    target_count = max(N, M // 2)
    
    words = []
    chars = "abcdefghijklmnopqrstuvwxyz"
    
    # Gerar palavras distintas usando produto cartesiano para tamanhos 1, 2, etc.
    # Precisamos de no máximo 10.000 palavras.
    # 26^1 + 26^2 = 26 + 676 = 702.
    # 26^3 = 17576. 
    # Logo, palavras de tamanho até 3 são suficientes para cobrir o máximo de 10.000.
    
    for length in range(1, 4):
        for p in itertools.product(chars, repeat=length):
            words.append("".join(p))
            if len(words) == target_count:
                break
        if len(words) == target_count:
            break
            
    # Imprimir a redação
    print(" ".join(words))

if __name__ == "__main__":
    solve()