A mancha é regular se e somente se para todo par de pixels P, Q na mancha, d(P,Q) = dmanhattan(P,Q). Isso significa que sempre existe um caminho Manhattan-ótimo dentro da mancha.

Uma condição equivalente: a mancha é regular se e somente se ela é "ortogonalmente convex" no sentido de que para qualquer dois pixels na mancha, existe um caminho de comprimento Manhattan entre eles dentro da mancha. 

Uma condição necessária e suficiente para isso é: para qualquer pixel (r,c) na mancha, e qualquer pixel (r',c') na mancha, todos os pixels no "retângulo" entre eles que formam um caminho Manhattan devem existir. Mais precisamente: a mancha é regular se e somente se:
1. Cada linha da mancha é um intervalo contíguo de colunas (ou vazia).
2. Cada coluna da mancha é um intervalo contíguo de linhas (ou vazia).
3. A "projeção" é convexa: se considerarmos as linhas com pixels, para qualquer duas linhas r1 < r2 que têm pixels, e colunas c1, c2 que estão em ambas as linhas, então todas as linhas entre r1 e r2 devem conter c1 e c2.

Na verdade, a condição exata é: cada linha é um segmento contíguo, cada coluna é um segmento contíguo, E para quaisquer duas linhas r1 < r2, o intervalo de colunas da linha r1 e o intervalo de colunas da linha r2 devem se "sobrepor" de forma que qualquer coluna presente em ambas esteja presente em todas as linhas intermediárias. Isso equivale a: a interseção dos intervalos de colunas de r1 e r2 deve estar contida no intervalo de colunas de cada linha intermediária.

Simplificando: condição suficiente e necessária é que cada linha seja contígua, cada coluna seja contígua, e para quaisquer r1 ≤ r ≤ r2, [col_min(r1), col_max(r1)] ∩ [col_min(r2), col_max(r2)] ⊆ [col_min(r), col_max(r)].

```python
import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    grid = []
    for i in range(n):
        grid.append(data[idx]); idx += 1
    
    row_min = {}
    row_max = {}
    col_min = {}
    col_max = {}
    
    for r in range(n):
        for c in range(n):
            if grid[r][c] == '*':
                if r not in row_min:
                    row_min[r] = c
                    row_max[r] = c
                else:
                    row_min[r] = min(row_min[r], c)
                    row_max[r] = max(row_max[r], c)
                if c not in col_min:
                    col_min[c] = r
                    col_max[c] = r
                else:
                    col_min[c] = min(col_min[c], r)
                    col_max[c] = max(col_max[c], r)
    
    # Check each row is contiguous
    for r in row_min:
        for c in range(row_min[r], row_max[r]+1):
            if grid[r][c] != '*':
                print("N")
                return
    
    # Check each column is contiguous
    for c in col_min:
        for r in range(col_min[c], col_max[c]+1):
            if grid[r][c] != '*':
                print("N")
                return
    
    # Check: for any two rows r1 < r2, intersection of their col intervals
    # must be subset of col interval of every row r between them
    rows = sorted(row_min.keys())
    for i in range(len(rows)):
        for j in range(i+1, len(rows)):
            r1 = rows[i]
            r2 = rows[j]
            inter_lo = max(row_min[r1], row_min[r2])
            inter_hi = min(row_max[r1], row_max[r2])
            if inter_lo > inter_hi:
                continue
            # All rows between r1 and r2 must contain [inter_lo, inter_hi]
            for r in range(r1+1, r2):
                if r not in row_min:
                    print("N")
                    return
                if row_min[r] > inter_lo or row_max[r] < inter_hi:
                    print("N")
                    return
    
    print("S")

solve()
```