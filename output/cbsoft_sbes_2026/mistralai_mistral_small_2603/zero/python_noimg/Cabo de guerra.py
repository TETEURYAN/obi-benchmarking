
def main():
    forca = list(map(int, input().split()))
    total = sum(forca)
    if total % 2 != 0:
        print('N')
        return
    alvo = total // 2
    forca.sort()
    n = len(forca)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if forca[i] + forca[j] + forca[k] == alvo:
                    print('S')
                    return
    print('N')

if __name__ == '__main__':
    main()
