import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    grid = [input().strip() for _ in range(N)]

    rows = []
    cols = []

    for i in range(N):
        line = grid[i]
        first = line.find('*')
        if first != -1:
            last = line.rfind('*')
            if '.' in line[first:last+1]:
                print('N')
                return
            rows.append((i, first, last))
            cols.append((first, last))

    if not rows:
        print('N')
        return

    prev_l, prev_r = cols[0]
    for l, r in cols[1:]:
        if r < prev_l or prev_r < l:
            print('N')
            return
        prev_l, prev_r = l, r

    print('S')

if __name__ == "__main__":
    main()
