
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    pieces = {}
    start = None

    for i in range(1, n + 1):
        e = int(data[3*i - 2])
        c = data[3*i - 1]
        d = int(data[3*i])
        pieces[e] = (c, d)
        if e == 0:
            start = e

    current = start
    result = []
    while current in pieces:
        c, d = pieces[current]
        result.append(c)
        current = d

    print(''.join(result))

if __name__ == "__main__":
    main()
