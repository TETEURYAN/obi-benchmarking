
def main():
    X, Y = map(int, input().split())
    L1, H1 = map(int, input().split())
    L2, H2 = map(int, input().split())

    def rotate(dim1, dim2):
        return (dim2, dim1)

    def can_fit(w1, h1, w2, h2):
        if (w1 + w2 <= X and max(h1, h2) <= Y) or (max(w1, w2) <= X and h1 + h2 <= Y):
            return True
        if (w1 + h2 <= X and max(h1, w2) <= Y) or (max(w1, h2) <= X and h1 + w2 <= Y):
            return True
        if (h1 + w2 <= X and max(w1, h2) <= Y) or (max(h1, w2) <= X and w1 + h2 <= Y):
            return True
        if (h1 + h2 <= X and max(w1, w2) <= Y) or (max(h1, h2) <= X and w1 + w2 <= Y):
            return True
        return False

    if can_fit(L1, H1, L2, H2):
        print('S')
        return

    L1, H1 = rotate(L1, H1)
    if can_fit(L1, H1, L2, H2):
        print('S')
        return

    L2, H2 = rotate(L2, H2)
    if can_fit(L1, H1, L2, H2):
        print('S')
        return

    L1, H1 = rotate(L1, H1)
    if can_fit(L1, H1, L2, H2):
        print('S')
        return

    print('N')

if __name__ == '__main__':
    main()
