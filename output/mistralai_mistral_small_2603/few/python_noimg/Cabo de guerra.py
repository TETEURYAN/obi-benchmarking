
import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    if len(data) != 6:
        print('N')
        return

    forces = data
    total = sum(forces)
    if total % 2 != 0:
        print('N')
        return

    target = total // 2
    found = False

    from itertools import combinations
    for team in combinations(forces, 3):
        if sum(team) == target:
            found = True
            break

    print('S' if found else 'N')

if __name__ == '__main__':
    main()
