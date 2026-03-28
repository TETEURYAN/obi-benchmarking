import sys
import itertools

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    pesos = list(map(int, data))
    total = sum(pesos)
    if total % 3 != 0:
        print('N')
        return
    x = total // 3
    if pesos.count(x) != 1:
        print('N')
        return
    for comb in itertools.combinations(pesos, 3):
        if sum(comb) == x:
            print('S')
            return
    print('N')

if __name__ == '__main__':
    main()