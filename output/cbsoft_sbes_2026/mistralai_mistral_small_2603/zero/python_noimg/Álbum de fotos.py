
def main():
    X, Y = map(int, input().split())
    L1, H1 = map(int, input().split())
    L2, H2 = map(int, input().split())

    def can_fit(a, b, c, d):
        return (a <= c and b <= d) or (a <= d and b <= c)

    possible = False

    # Caso 1: ambas fotos na orientação original
    if can_fit(L1, H1, X, Y) and can_fit(L2, H2, X, Y):
        # Verificar se as fotos cabem lado a lado ou uma acima da outra
        if (L1 + L2 <= X and max(H1, H2) <= Y) or \
           (max(L1, L2) <= X and H1 + H2 <= Y) or \
           (L1 + H2 <= X and max(H1, L2) <= Y) or \
           (H1 + L2 <= X and max(L1, H2) <= Y) or \
           (H1 + H2 <= X and max(L1, L2) <= Y) or \
           (L1 + L2 <= Y and max(H1, H2) <= X):
            possible = True

    # Caso 2: primeira foto girada, segunda original
    if not possible:
        if can_fit(H1, L1, X, Y) and can_fit(L2, H2, X, Y):
            if (H1 + L2 <= X and max(L1, H2) <= Y) or \
               (L1 + H2 <= X and max(H1, L2) <= Y) or \
               (max(H1, L2) <= X and L1 + H2 <= Y) or \
               (max(L1, H2) <= X and H1 + L2 <= Y) or \
               (H1 + H2 <= X and max(L1, L2) <= Y) or \
               (L1 + L2 <= Y and max(H1, H2) <= X):
                possible = True

    # Caso 3: primeira foto original, segunda girada
    if not possible:
        if can_fit(L1, H1, X, Y) and can_fit(H2, L2, X, Y):
            if (L1 + H2 <= X and max(H1, L2) <= Y) or \
               (H1 + L2 <= X and max(L1, H2) <= Y) or \
               (max(L1, H2) <= X and H1 + L2 <= Y) or \
               (max(H1, L2) <= X and L1 + H2 <= Y) or \
               (H1 + H2 <= X and max(L1, L2) <= Y) or \
               (L1 + L2 <= Y and max(H1, H2) <= X):
                possible = True

    # Caso 4: ambas fotos giradas
    if not possible:
        if can_fit(H1, L1, X, Y) and can_fit(H2, L2, X, Y):
            if (H1 + H2 <= X and max(L1, L2) <= Y) or \
               (L1 + L2 <= X and max(H1, H2) <= Y) or \
               (max(H1, H2) <= X and L1 + L2 <= Y) or \
               (max(L1, L2) <= X and H1 + H2 <= Y) or \
               (H1 + L2 <= X and max(L1, H2) <= Y) or \
               (L1 + H2 <= X and max(H1, L2) <= Y):
                possible = True

    print('S' if possible else 'N')

if __name__ == '__main__':
    main()
