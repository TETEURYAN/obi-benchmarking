
import sys

def main():
    try:
        # Leitura da entrada
        n_input = sys.stdin.readline()
        if not n_input:
            return
        N = int(n_input)
        
        line2 = sys.stdin.readline().split()
        X1, Y1 = int(line2[0]), int(line2[1])
        
        line3 = sys.stdin.readline().split()
        X2, Y2 = int(line3[0]), int(line3[1])
        
        half = N // 2
        
        # Verificar corte horizontal
        # Um quadrado deve estar na metade superior (X <= half) e outro na inferior (X > half)
        horizontal = (X1 <= half and X2 > half) or (X2 <= half and X1 > half)
        
        # Verificar corte vertical
        # Um quadrado deve estar na metade esquerda (Y <= half) e outro na direita (Y > half)
        vertical = (Y1 <= half and Y2 > half) or (Y2 <= half and Y1 > half)
        
        if horizontal or vertical:
            print("S")
        else:
            print("N")
            
    except Exception:
        return

if __name__ == "__main__":
    main()
