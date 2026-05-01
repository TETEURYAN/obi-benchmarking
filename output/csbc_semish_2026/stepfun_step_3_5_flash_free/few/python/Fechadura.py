import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    heights = list(map(int, data[2:2+n]))
    
    a = [h - m for h in heights]
    x = [0] * (n-1)
    x[0] = -a[0]
    for i in range(1, n-1):
        x[i] = -a[i] - x[i-1]
    
    # Verificação de consistência (opcional, pois o problema garante solução)
    if a[n-1] + x[n-2] != 0:
        # Caso não seja consistente, não há solução, mas o problema garante que há.
        # Poderíamos lançar erro, mas como é garantido, ignoramos.
        pass
    
    total_moves = sum(abs(val) for val in x)
    print(total_moves)

if __name__ == "__main__":
    main()