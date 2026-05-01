
import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    pieces = {}
    start = None
    for line in data[1:n+1]:
        e, c, d = line.split()
        e = int(e)
        d = int(d)
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
