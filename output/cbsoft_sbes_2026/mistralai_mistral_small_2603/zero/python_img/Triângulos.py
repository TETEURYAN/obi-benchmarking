
def main():
    A, B, C = map(int, input().split())
    lados = sorted([A, B, C])
    a, b, c = lados

    if a + b <= c:
        print('n')
        return

    a2 = a * a
    b2 = b * b
    c2 = c * c

    if a2 + b2 > c2:
        print('a')
    elif a2 + b2 == c2:
        print('r')
    else:
        print('o')

if __name__ == "__main__":
    main()
