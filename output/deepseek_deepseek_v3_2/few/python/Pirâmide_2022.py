import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    N = int(data[0])
    pyramid = [[0] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            # A camada é determinada pela distância mínima até a borda
            layer = min(i, j, N - 1 - i, N - 1 - j) + 1
            pyramid[i][j] = layer
    
    out_lines = [' '.join(map(str, row)) for row in pyramid]
    sys.stdout.write('\n'.join(out_lines))

if __name__ == "__main__":
    main()