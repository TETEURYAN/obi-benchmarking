import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    X, Y = int(data[0]), int(data[1])
    L1, H1 = int(data[2]), int(data[3])
    L2, H2 = int(data[4]), int(data[5])
    
    # Possíveis orientações das fotos: (largura, altura)
    orientacoes1 = [(L1, H1), (H1, L1)]
    orientacoes2 = [(L2, H2), (H2, L2)]
    
    for w1, h1 in orientacoes1:
        for w2, h2 in orientacoes2:
            # Verifica se as fotos cabem individualmente na página
            if w1 <= X and h1 <= Y and w2 <= X and h2 <= Y:
                # Tenta colocar lado a lado (horizontalmente)
                # A soma das larguras deve ser <= X e a altura máxima <= Y
                if (w1 + w2 <= X and max(h1, h2) <= Y):
                    print('S')
                    return
                # Tenta colocar uma sobre a outra (verticalmente)
                # A soma das alturas deve ser <= Y e a largura máxima <= X
                if (h1 + h2 <= Y and max(w1, w2) <= X):
                    print('S')
                    return
                    
    print('N')

if __name__ == '__main__':
    solve()