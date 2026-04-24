import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    n1, d1, v1 = map(int, data[:3])
    n2, d2, v2 = map(int, data[3:6])
    
    # Converter velocidade de km/h para m/s
    v1_ms = v1 * (1000 / 3600)
    v2_ms = v2 * (1000 / 3600)
    
    # Calcular tempo até a linha de chegada
    t1 = d1 / v1_ms
    t2 = d2 / v2_ms
    
    # Determinar o vencedor (menor tempo)
    if t1 < t2:
        print(n1)
    else:
        print(n2)

if __name__ == "__main__":
    main()