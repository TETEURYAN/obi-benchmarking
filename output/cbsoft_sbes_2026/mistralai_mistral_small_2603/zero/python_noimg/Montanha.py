
def main():
    n = int(input())
    alturas = list(map(int, input().split()))
    tem_mais_de_um_pico = False

    for i in range(1, n-1):
        if alturas[i-1] > alturas[i] and alturas[i] < alturas[i+1]:
            tem_mais_de_um_pico = True
            break

    print('S' if tem_mais_de_um_pico else 'N')

if __name__ == '__main__':
    main()
