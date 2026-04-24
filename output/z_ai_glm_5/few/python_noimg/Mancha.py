import sys

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # O primeiro elemento é N, o tamanho da grade
    n = int(input_data[0])
    
    # Os próximos N elementos são as linhas da grade
    grid = input_data[1:n+1]
    
    # Verificação de convexidade ortogonal (regularidade da mancha)
    # Uma mancha é regular se e somente se for ortogonalmente convexa.
    # Isso significa que a interseção da mancha com qualquer linha horizontal 
    # ou vertical deve ser um segmento único e contínuo.
    
    # 1. Verificar linhas horizontais
    for r in range(n):
        row = grid[r]
        # Dividimos a linha pelos pixels vazios '.'
        # Se houver mais de um segmento contínuo de '*', a mancha é irregular
        segments = row.split('.')
        count = 0
        for seg in segments:
            if '*' in seg:
                count += 1
                if count > 1:
                    print("N")
                    return
                    
    # 2. Verificar linhas verticais
    for c in range(n):
        found_star = False
        found_gap = False
        for r in range(n):
            if grid[r][c] == '*':
                if found_gap:
                    # Encontramos um '*' após um espaço '.', o que significa
                    # que existem dois segmentos separados na mesma coluna
                    print("N")
                    return
                found_star = True
            else:
                # Se já encontramos um '*' e agora vemos um '.', entramos em um espaço
                if found_star:
                    found_gap = True
    
    # Se passou por todas as linhas e colunas sem encontrar descontinuidades
    print("S")

if __name__ == '__main__':
    solve()