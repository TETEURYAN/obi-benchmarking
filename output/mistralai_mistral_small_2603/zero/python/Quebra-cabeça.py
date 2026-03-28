
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    pieces = {}
    lefts = {}
    rights = {}
    for i in range(1, n+1):
        e = int(data[3*i - 2])
        c = data[3*i - 1]
        d = int(data[3*i])
        pieces[e] = (c, d)
        lefts[e] = True
        rights[d] = True

    current = 0
    result = []
    while current in pieces:
        c, d = pieces[current]
        result.append(c)
        current = d

    print(''.join(result))

if __name__ == "__main__":
    main()
