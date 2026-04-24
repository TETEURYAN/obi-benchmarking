import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    forces = list(map(int, data))
    total = sum(forces)
    if total % 2 != 0:
        print('N')
        return
    target = total // 2
    from itertools import combinations
    for comb in combinations(range(6), 3):
        s = forces[comb[0]] + forces[comb[1]] + forces[comb[2]]
        if s == target:
            print('S')
            return
    print('N')

if __name__ == "__main__":
    main()