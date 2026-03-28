import sys

# Aumentar o limite de recursão para evitar erros em casos de fundo de pilha,
# embora a implementação do Merge Sort seja iterativa ou com profundidade log(N).
sys.setrecursionlimit(200000)

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        N = int(next(iterator))
        P = int(next(iterator))
        Q = int(next(iterator))
    except StopIteration:
        return

    points = []
    for _ in range(N):
        x = int(next(iterator))
        y = int(next(iterator))
        points.append((x, y))

    # Passo 1: Ordenar os pontos pela coordenada X.
    # O problema garante que não existem dois titãs com a mesma coordenada X.
    points.sort()

    # Passo 2: Calcular o valor transformado para cada ponto.
    # A condição (Ya - Yb) / (Xa - Xb) >= P/Q
    # Se Xa < Xb, a condição se torna Q*Ya - P*Xa <= Q*Yb - P*Xb.
    # Se Q < 0, a desigualdade inverte ao multiplicar por Q.
    # Para unificar, definimos Val = Q*Y - P*X.
    # Se Q > 0, queremos contar pares (i, j) com i < j e Val[i] <= Val[j].
    # Se Q < 0, a desigualdade inverte, então queremos Val[i] >= Val[j].
    # Podemos simplesmente inverter o sinal de Val se Q < 0, reduzindo ao caso Val[i] <= Val[j].
    
    vals = []
    for x, y in points:
        vals.append(Q * y - P * x)
    
    if Q < 0:
        # Se Q é negativo, a condição original para Xa < Xb era Val_a >= Val_b.
        # Multiplicando por -1, queremos -Val_a <= -Val_b.
        vals = [-v for v in vals]

    # Passo 3: Contar pares (i, j) com i < j e vals[i] <= vals[j].
    # Isso é equivalente a: Total de Pares - Pares de Inversão (vals[i] > vals[j]).
    # Total de pares = N * (N - 1) / 2.
    
    total_pairs = N * (N - 1) // 2
    
    # Contagem de inversões usando Merge Sort
    # Complexidade: O(N log N)
    
    def count_inversions(arr):
        n = len(arr)
        temp = [0] * n
        return _merge_sort(arr, temp, 0, n - 1)

    def _merge_sort(arr, temp, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2
            inv_count += _merge_sort(arr, temp, left, mid)
            inv_count += _merge_sort(arr, temp, mid + 1, right)
            inv_count += merge(arr, temp, left, mid, right)
        return inv_count

    def merge(arr, temp, left, mid, right):
        i = left
        j = mid + 1
        k = left
        inv_count = 0
        
        while i <= mid and j <= right:
            # Para contar inversões, procuramos arr[i] > arr[j] com i < j.
            # Como i está na metade esquerda (índices menores) e j na direita (maiores),
            # se arr[i] > arr[j], então todos os elementos de i até mid são maiores que arr[j].
            if arr[i] > arr[j]:
                temp[k] = arr[j]
                inv_count += (mid - i + 1)
                j += 1
            else:
                temp[k] = arr[i]
                i += 1
            k += 1
        
        while i <= mid:
            temp[k] = arr[i]
            i += 1
            k += 1
            
        while j <= right:
            temp[k] = arr[j]
            j += 1
            k += 1
            
        for idx in range(left, right + 1):
            arr[idx] = temp[idx]
            
        return inv_count

    inversions = count_inversions(vals)
    
    result = total_pairs - inversions
    
    print(result)

if __name__ == '__main__':
    solve()