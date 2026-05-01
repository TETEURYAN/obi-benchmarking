import sys

def main():
    # Leitura rápida do input
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    n = int(input_data[0])

    # Cálculo dos cubinhos:
    # 3 faces: Apenas os vértices (cantos) do cubo. Sempre 8.
    tres_faces = 8

    # 2 faces: Arestas do cubo, excluindo os vértices.
    # Existem 12 arestas em um cubo. Cada aresta tem (N - 2) cubinhos centrais.
    duas_faces = 12 * (n - 2)

    # 1 face: Centro das faces do cubo, excluindo as arestas.
    # Existem 6 faces. Cada face tem uma grade (N-2) x (N-2) de cubinhos centrais.
    uma_face = 6 * (n - 2) ** 2

    # 0 faces: Interior do cubo.
    # É um cubo menor de lado (N - 2).
    nenhuma_face = (n - 2) ** 3

    # Imprimindo os resultados na ordem solicitada
    print(nenhuma_face)
    print(uma_face)
    print(duas_faces)
    print(tres_faces)

if __name__ == "__main__":
    main()