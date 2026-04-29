import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    L = data[1:1+n]

    total = sum(L)
    if total % 2 != 0:
        print('N')
        return

    half = total // 2

    pos = [0]
    s = 0
    for x in L[:-1]:
        s += x
        pos.append(s)

    points = set(pos)

    diam_count = 0
    for p in pos:
        if p + half in points:
            diam_count += 1

    print('S' if diam_count >= 2 else 'N')

if __name__ == "__main__":
    main()
