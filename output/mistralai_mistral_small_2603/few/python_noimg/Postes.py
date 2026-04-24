import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    postes = list(map(int, data[1:n+1]))
    
    substituir = 0
    consertar = 0
    
    for x in postes:
        if x < 50:
            substituir += 1
        elif x < 85:
            consertar += 1
    
    print(f"{substituir} {consertar}")

if __name__ == "__main__":
    main()