import sys

def cabe_duas(X, Y, a, b, c, d):
    return (max(a, c) <= X and b + d <= Y) or (a + c <= X and max(b, d) <= Y)

def main():
    data = list(map(int, sys.stdin.read().split()))
    X, Y = data[0], data[1]
    l1, h1 = data[2], data[3]
    l2, h2 = data[4], data[5]

    possivel = False
    for a, b in ((l1, h1), (h1, l1)):
        for c, d in ((l2, h2), (h2, l2)):
            if cabe_duas(X, Y, a, b, c, d):
                possivel = True
                break
        if possivel:
            break

    print('S' if possivel else 'N')

if __name__ == "__main__":
    main()
