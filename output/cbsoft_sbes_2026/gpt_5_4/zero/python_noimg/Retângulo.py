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

    pos = 0
    seen = {0}
    for x in L[:-1]:
        pos += x
        seen.add(pos)

    for p in seen:
        if p + half in seen:
            print('S')
            return

    print('N')

if __name__ == "__main__":
    main()
