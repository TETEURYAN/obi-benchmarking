
import sys
import bisect

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    p = int(data[1])
    q = int(data[2])
    points = []
    idx = 3
    for i in range(n):
        x = int(data[idx])
        y = int(data[idx+1])
        points.append((x, y))
        idx += 2

    # Ordenar por x
    points.sort(key=lambda p: p[0])

    # Transformação: y_i - (p/q) * x_i
    # Cuidado com divisão por zero e frações
    # Multiplicar por q para evitar divisão
    transformed = []
    for x, y in points:
        val = y * q - p * x
        transformed.append(val)

    # Para cada ponto, contar quantos j > i têm transformed[j] >= transformed[i]
    # Isso é equivalente a contar para cada i, número de elementos no suffixo >= transformed[i]
    # Podemos usar Fenwick Tree ou ordenação reversa.

    # Ordenar transformed para contar inversos de "não decrescentes"
    sorted_vals = sorted(transformed)
    total = 0
    # Usar Fenwick Tree (BIT) para contar elementos maiores ou igual
    # Construir BIT sobre valores comprimidos
    # Primeiro, comprimir coordenadas
    comp = {}
    unique_vals = sorted(set(sorted_vals))
    for idx, val in enumerate(unique_vals):
        comp[val] = idx + 1  # BIT indexado de 1

    m = len(unique_vals)
    bit = [0] * (m + 2)

    def bit_update(idx, delta):
        while idx <= m + 1:
            bit[idx] += delta
            idx += idx & -idx

    def bit_query(idx):
        s = 0
        while idx > 0:
            s += bit[idx]
            idx -= idx & -idx
        return s

    # Processar de trás para frente
    for i in range(n - 1, -1, -1):
        val = transformed[i]
        pos = comp[val]
        # Quantos já processados têm valor >= val?
        # BIT armazena frequências dos já processados.
        # Para >= val, query(m+1) - query(pos-1)
        count = bit_query(m + 1) - bit_query(pos - 1)
        total += count
        bit_update(pos, 1)

    print(total)

if __name__ == "__main__":
    main()
