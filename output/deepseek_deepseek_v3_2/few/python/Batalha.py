import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    a1 = int(data[0])
    d1 = int(data[1])
    a2 = int(data[2])
    d2 = int(data[3])
    
    # Regras: um monstrinho desmaia se sua defesa != ataque do oponente
    desmaia1 = d1 != a2
    desmaia2 = d2 != a1
    
    if not desmaia1 and desmaia2:
        print(1)
    elif desmaia1 and not desmaia2:
        print(2)
    else:
        print(-1)

if __name__ == "__main__":
    main()