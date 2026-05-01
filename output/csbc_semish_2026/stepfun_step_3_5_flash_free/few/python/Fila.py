import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    fila = list(map(int, data[1:1+n]))
    m = int(data[1+n])
    sairam = list(map(int, data[2+n:2+n+m]))
    set_sairam = set(sairam)
    resultado = [x for x in fila if x not in set_sairam]
    print(' '.join(map(str, resultado)))

if __name__ == "__main__":
    main()