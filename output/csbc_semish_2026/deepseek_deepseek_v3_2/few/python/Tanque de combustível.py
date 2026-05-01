import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    C = int(data[0])
    D = int(data[1])
    T = int(data[2])
    
    litros_necessarios = D / C
    comprar = litros_necessarios - T
    if comprar < 0:
        comprar = 0.0
    print(f"{comprar:.1f}")

if __name__ == "__main__":
    main()