
def main():
    pesos = list(map(int, input().split()))
    pesos.sort()
    total = sum(pesos)
    if total % 3 != 0:
        print('N')
        return
    target = total // 3
    if pesos[0] + pesos[1] + pesos[2] == target and pesos[3] + pesos[4] == target and pesos[5] == target:
        print('S')
    else:
        print('N')

if __name__ == '__main__':
    main()
