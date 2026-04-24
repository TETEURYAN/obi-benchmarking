import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    N = int(data[0])
    R = int(data[1])
    P = int(data[2])
    
    total = N
    if total >= P:
        print(0)
        return
    
    infectados_hoje = N
    dia = 0
    while total < P:
        dia += 1
        infectados_hoje *= R
        total += infectados_hoje
    print(dia)

if __name__ == "__main__":
    main()