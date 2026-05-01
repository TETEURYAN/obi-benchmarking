import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    idx = 0
    test_num = 1
    output_lines = []
    
    while idx < len(data):
        N = int(data[idx])
        idx += 1
        if N == -1:
            break
        
        # Cada dobra D reduz o tamanho para 1/4, mas aumenta o número de camadas.
        # Após N dobras, temos 4^N camadas (cada dobra multiplica por 4).
        # Corte vertical e horizontal divide cada camada em 4 pedaços.
        # Total = (4^N) * 4 = 4^(N+1)
        pieces = 4 ** (N + 1)
        
        output_lines.append(f"Teste {test_num}")
        output_lines.append(str(pieces))
        output_lines.append("")
        test_num += 1
    
    sys.stdout.write("\n".join(output_lines))

if __name__ == "__main__":
    main()