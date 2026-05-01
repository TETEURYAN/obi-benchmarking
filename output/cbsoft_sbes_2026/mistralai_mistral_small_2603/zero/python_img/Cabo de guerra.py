
def main():
    X = list(map(int, input().split()))
    total = sum(X)
    if total % 2 != 0:
        print('N')
        return
    target = total // 2
    from itertools import combinations
    for team in combinations(X, 3):
        if sum(team) == target:
            print('S')
            return
    print('N')

if __name__ == '__main__':
    main()
