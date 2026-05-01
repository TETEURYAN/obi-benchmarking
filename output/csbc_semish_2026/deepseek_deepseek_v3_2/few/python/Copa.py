import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    K = int(data[0])
    L = int(data[1])
    
    # Ajusta para índice 0-15
    k = K - 1
    l = L - 1
    
    # Fase 1: oitavas (grupos de 2)
    if k // 2 == l // 2:
        print("oitavas")
        return
    
    # Fase 2: quartas (grupos de 4)
    if k // 4 == l // 4:
        print("quartas")
        return
    
    # Fase 3: semifinal (grupos de 8)
    if k // 8 == l // 8:
        print("semifinal")
        return
    
    # Caso contrário: final
    print("final")

if __name__ == "__main__":
    main()