
def main():
    pesos = list(map(int, input().split()))
    pesos.sort(reverse=True)
    total = sum(pesos)
    if total % 3 != 0:
        print('N')
        return
    target = total // 3
    if pesos[0] > target:
        print('N')
        return
    if len(pesos) == 6:
        a, b, c, d, e, f = pesos
        if (a + b + c == target and d + e == target and f == target) or \
           (a + b + d == target and c + e == target and f == target) or \
           (a + b + e == target and c + d == target and f == target) or \
           (a + c + d == target and b + e == target and f == target) or \
           (a + c + e == target and b + d == target and f == target) or \
           (a + d + e == target and b + c == target and f == target):
            print('S')
        else:
            print('N')
    else:
        print('N')

if __name__ == '__main__':
    main()
