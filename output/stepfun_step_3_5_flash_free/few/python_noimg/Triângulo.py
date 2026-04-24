import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    a, b, c, d = map(int, data)
    combos = [(a, b, c), (a, b, d), (a, c, d), (b, c, d)]
    for x, y, z in combos:
        tri = sorted((x, y, z))
        if tri[0] + tri[1] > tri[2]:
            print('S')
            return
    print('N')

if __name__ == "__main__":
    main()