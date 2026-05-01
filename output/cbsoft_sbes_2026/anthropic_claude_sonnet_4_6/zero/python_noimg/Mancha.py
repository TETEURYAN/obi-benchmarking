from collections import deque
import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    grid = []
    for _ in range(N):
        grid.append(input().strip())
    
    # A mancha é regular se e somente se para qualquer par P, Q:
    # d(P,Q) = dmanhattan(P,Q)
    # 
    # Isso significa que sempre existe um caminho de comprimento mínimo igual à distância Manhattan.
    # Isso é equivalente a dizer que a mancha é "ortogonalmente convex" no sentido de Manhattan.
    # 
    # Uma condição necessária e suficiente: a mancha é regular se e somente se
    # para cada par de pixels P e Q na mancha, o "retângulo" de Manhattan entre eles
    # pode ser percorrido sem sair da mancha - mais precisamente, não há "buracos" ou
    # "reentrâncias" que forcem desvios.
    #
    # Na verdade, a condição equivalente é:
    # A mancha é regular se e somente se ela é "HV-convex" E "HV-connected":
    # - Cada linha da mancha forma um intervalo contíguo (ou vazio)
    # - Cada coluna da mancha forma um intervalo contíguo (ou vazio)
    # 
    # Isso garante que d(P,Q) = dmanhattan(P,Q) para todo par.
    # 
    # Prova: Se linhas e colunas são intervalos contíguos, então dado P=(r1,c1) e Q=(r2,c2),
    # podemos ir de P para Q movendo linha a linha e coluna a coluna sem sair da mancha.
    
    # Verificar se cada linha tem pixels contíguos
    for i in range(N):
        row = grid[i]
        first = -1
        last = -1
        for j in range(N):
            if row[j] == '*':
                if first == -1:
                    first = j
                last = j
        if first != -1:
            # Verificar que todos entre first e last são '*'
            for j in range(first, last+1):
                if row[j] != '*':
                    print("N")
                    return
    
    # Verificar se cada coluna tem pixels contíguos
    for j in range(N):
        first = -1
        last = -1
        for i in range(N):
            if grid[i][j] == '*':
                if first == -1:
                    first = i
                last = i
        if first != -1:
            for i in range(first, last+1):
                if grid[i][j] != '*':
                    print("N")
                    return
    
    print("S")

solve()