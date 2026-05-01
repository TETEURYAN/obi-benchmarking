import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    pesos = list(map(int, data[1:1+n]))
    pesos.sort()
    i = 0
    while i < n:
        j = i
        while j + 1 < n and pesos[j+1] - pesos[j] <= 8:
            j += 1
        tem_leve = any(pesos[k] <= 8 for k in range(i, j+1))
        if not tem_leve:
            print('N')
            return
        i = j + 1
    print('S')

if __name__ == '__main__':
    main()