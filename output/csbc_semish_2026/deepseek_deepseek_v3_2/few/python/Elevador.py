import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    weights = list(map(int, data[1:1 + n]))
    
    # Ordena os pesos para facilitar o emparelhamento
    weights.sort()
    
    # Se houver apenas uma caixa, sempre é possível
    if n == 1:
        print("S")
        return
    
    # Verifica se existe algum par de caixas com diferença > 8
    # Se existir, não é possível, pois essas duas caixas nunca poderão
    # estar simultaneamente no elevador em viagens diferentes.
    # A estratégia é: para cada caixa, deve haver outra caixa
    # que possa ser seu contrapeso (diferença <= 8) em algum momento.
    # Isso equivale a verificar se podemos emparelhar as caixas
    # em grupos onde a diferença máxima dentro de cada grupo é <= 8.
    # Uma condição necessária e suficiente é que, após ordenar,
    # a diferença entre quaisquer duas caixas adjacentes na ordem
    # seja <= 8. Porque se houver um salto maior que 8, as caixas
    # do lado esquerdo do salto nunca poderão encontrar contrapeso
    # nas do lado direito.
    for i in range(1, n):
        if weights[i] - weights[i - 1] > 8:
            print("N")
            return
    
    print("S")

if __name__ == "__main__":
    solve()