import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    grid = [input().strip() for _ in range(N)]

    rows = []
    cols = []

    for i in range(N):
        row = grid[i]
        js = [j for j, ch in enumerate(row) if ch == '*']
        if js:
            rows.append((i, js[0], js[-1]))
            cols.extend(js)

    min_r = rows[0][0]
    max_r = rows[-1][0]
    min_c = min(cols)
    max_c = max(cols)

    prev_l = prev_r = None
    started = False

    for i in range(min_r, max_r + 1):
        row = grid[i]
        l = row.find('*')
        r = row.rfind('*')

        if l == -1:
            print("N")
            return

        for j in range(l, r + 1):
            if row[j] != '*':
                print("N")
                return

        if not started:
            started = True
            prev_l, prev_r = l, r
            continue

        if r < prev_l - 1 or l > prev_r + 1:
            print("N")
            return

        prev_l, prev_r = l, r

    for j in range(min_c, max_c + 1):
        top = -1
        bottom = -1
        for i in range(min_r, max_r + 1):
            if grid[i][j] == '*':
                if top == -1:
                    top = i
                bottom = i

        if top == -1:
            print("N")
            return

        for i in range(top, bottom + 1):
            if grid[i][j] != '*':
                print("N")
                return

    print("S")

if __name__ == "__main__":
    main()
