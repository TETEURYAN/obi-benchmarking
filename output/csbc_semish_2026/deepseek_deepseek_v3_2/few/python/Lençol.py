import sys

def can_form(a1, b1, a2, b2, A, B):
    # Função auxiliar para testar se dois retângulos podem formar o lençol
    def test(x1, y1, x2, y2, X, Y):
        # Caso 1: Colocar um ao lado do outro (soma de larguras)
        if max(y1, y2) <= Y and x1 + x2 <= X:
            return True
        # Caso 2: Colocar um sobre o outro (soma de alturas)
        if max(x1, x2) <= X and y1 + y2 <= Y:
            return True
        return False

    # Testar todas as rotações possíveis dos retângulos (0° e 90°)
    for r1 in [(a1, b1), (b1, a1)]:
        for r2 in [(a2, b2), (b2, a2)]:
            # Testar ambas as orientações do lençol (A×B e B×A)
            if test(r1[0], r1[1], r2[0], r2[1], A, B) or \
               test(r1[0], r1[1], r2[0], r2[1], B, A):
                return True
    return False

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    a1, b1, a2, b2, A, B = map(int, data)
    result = 'S' if can_form(a1, b1, a2, b2, A, B) else 'N'
    print(result)

if __name__ == "__main__":
    main()