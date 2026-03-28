import sys
sys.setrecursionlimit(1 << 25)

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    X = [int(next(it)) for _ in range(n)]
    Y = [int(next(it)) for _ in range(n)]

    points = list(zip(X, Y))
    
    # Transformações de coordenadas
    # (x, y) -> (x+y, x-y)  (rotação 45º + escala)
    # A distância de Chebyshev no espaço transformado corresponde à distância Manhattan original
    # max(|x1-x2|, |y1-y2|) no transformado = |x1-x2| + |y1-y2| no original
    # Mas aqui queremos minimizar o máximo da distância Manhattan entre pontos do mesmo grupo.
    # Isso é equivalente a minimizar o máximo da distância de Chebyshev no espaço transformado.
    
    # Vamos trabalhar com as 4 combinações de sinais:
    # a =  x + y
    # b =  x - y
    # c = -x + y
    # d = -x - y
    # Para dois pontos p e q, a distância Manhattan é max(a_p - a_q, b_p - b_q, c_p - c_q, d_p - d_q)
    # entre as 4 combinações.
    
    # Vamos calcular os valores extremos para cada uma das 4 funções.
    a_vals = [x + y for x, y in points]
    b_vals = [x - y for x, y in points]
    c_vals = [-x + y for x, y in points]
    d_vals = [-x - y for x, y in points]
    
    min_a, max_a = min(a_vals), max(a_vals)
    min_b, max_b = min(b_vals), max(b_vals)
    min_c, max_c = min(c_vals), max(c_vals)
    min_d, max_d = min(d_vals), max(d_vals)
    
    # A resposta é o menor valor D tal que podemos particionar os pontos em dois grupos
    # onde dentro de cada grupo, para cada par, as 4 diferenças são <= D.
    # Isso significa que dentro de cada grupo, o intervalo de cada uma das 4 funções é <= D.
    # Ou seja, max_a - min_a <= D, max_b - min_b <= D, etc.
    
    # Vamos tentar particionar os pontos em dois grupos que satisfaçam isso.
    # Ideia: ordenar por uma das coordenadas transformadas e usar two pointers.
    # Mas com N até 300k, precisamos de O(N log N) ou O(N).
    
    # Observação: se fixarmos D, podemos verificar se é possível particionar em dois grupos.
    # Como? Escolha um ponto como referência para o grupo 1, todos os pontos que estão dentro
    # de "distância" D dele (nas 4 métricas) podem estar no mesmo grupo.
    # Se sobrar algum ponto fora, ele deve formar o grupo 2, e todos os pontos do grupo 2
    # também devem estar dentro de D entre si.
    # Isso se reduz a: existe um ponto p tal que todos os pontos com distância > D de p
    # estão dentro de uma "bola" de raio D (nas 4 métricas) em torno de algum outro ponto q.
    
    # Vamos implementar a verificação para um D fixo.
    def can(D):
        # Encontra os pontos que estão dentro de D do ponto com menor a.
        # Vamos tentar duas estratégias:
        # 1. Grupo 1: pontos com a <= min_a + D, b entre [min_b, min_b+D], c entre [min_c, min_c+D], d entre [min_d, min_d+D]
        # Mas isso é muito restritivo. Melhor: grupo 1 é definido por um ponto semente.
        # Vamos tentar sementes nos extremos.
        
        # Se D é viável, então existe um grupo cujo intervalo de a é <= D.
        # Sem perda de generalidade, podemos assumir que esse grupo contém o ponto com menor a.
        # Então todos os pontos desse grupo devem ter a <= min_a + D.
        # Dentro desses pontos, os valores de b, c, d também devem ter intervalo <= D.
        # Vamos coletar os pontos com a <= min_a + D.
        candidates = [i for i in range(n) if a_vals[i] <= min_a + D]
        if not candidates:
            return False
        # Dentro desses, verificar se podemos escolher um subconjunto que forma um grupo válido.
        # Mas na verdade, se todos os pontos com a <= min_a + D não cabem num grupo de intervalo D,
        # então não tem como, porque qualquer grupo que contenha o ponto de min_a deve ter a <= min_a + D.
        # Então basta verificar se entre os pontos com a <= min_a + D, os intervalos de b, c, d são <= D.
        b_vals_sub = [b_vals[i] for i in candidates]
        c_vals_sub = [c_vals[i] for i in candidates]
        d_vals_sub = [d_vals[i] for i in candidates]
        if max(b_vals_sub) - min(b_vals_sub) <= D and max(c_vals_sub) - min(c_vals_sub) <= D and max(d_vals_sub) - min(d_vals_sub) <= D:
            return True
        
        # Tenta com o ponto de max_a
        candidates = [i for i in range(n) if a_vals[i] >= max_a - D]
        b_vals_sub = [b_vals[i] for i in candidates]
        c_vals_sub = [c_vals[i] for i in candidates]
        d_vals_sub = [d_vals[i] for i in candidates]
        if max(b_vals_sub) - min(b_vals_sub) <= D and max(c_vals_sub) - min(c_vals_sub) <= D and max(d_vals_sub) - min(d_vals_sub) <= D:
            return True
        
        # Tenta com o ponto de min_b
        candidates = [i for i in range(n) if b_vals[i] <= min_b + D]
        a_vals_sub = [a_vals[i] for i in candidates]
        c_vals_sub = [c_vals[i] for i in candidates]
        d_vals_sub = [d_vals[i] for i in candidates]
        if max(a_vals_sub) - min(a_vals_sub) <= D and max(c_vals_sub) - min(c_vals_sub) <= D and max(d_vals_sub) - min(d_vals_sub) <= D:
            return True
        
        # Tenta com o ponto de max_b
        candidates = [i for i in range(n) if b_vals[i] >= max_b - D]
        a_vals_sub = [a_vals[i] for i in candidates]
        c_vals_sub = [c_vals[i] for i in candidates]
        d_vals_sub = [d_vals[i] for i in candidates]
        if max(a_vals_sub) - min(a_vals_sub) <= D and max(c_vals_sub) - min(c_vals_sub) <= D and max(d_vals_sub) - min(d_vals_sub) <= D:
            return True
        
        # Tenta com o ponto de min_c
        candidates = [i for i in range(n) if c_vals[i] <= min_c + D]
        a_vals_sub = [a_vals[i] for i in candidates]
        b_vals_sub = [b_vals[i] for i in candidates]
        d_vals_sub = [d_vals[i] for i in candidates]
        if max(a_vals_sub) - min(a_vals_sub) <= D and max(b_vals_sub) - min(b_vals_sub) <= D and max(d_vals_sub) - min(d_vals_sub) <= D:
            return True
        
        # Tenta com o ponto de max_c
        candidates = [i for i in range(n) if c_vals[i] >= max_c - D]
        a_vals_sub = [a_vals[i] for i in candidates]
        b_vals_sub = [b_vals[i] for i in candidates]
        d_vals_sub = [d_vals[i] for i in candidates]
        if max(a_vals_sub) - min(a_vals_sub) <= D and max(b_vals_sub) - min(b_vals_sub) <= D and max(d_vals_sub) - min(d_vals_sub) <= D:
            return True
        
        # Tenta com o ponto de min_d
        candidates = [i for i in range(n) if d_vals[i] <= min_d + D]
        a_vals_sub = [a_vals[i] for i in candidates]
        b_vals_sub = [b_vals[i] for i in candidates]
        c_vals_sub = [c_vals[i] for i in candidates]
        if max(a_vals_sub) - min(a_vals_sub) <= D and max(b_vals_sub) - min(b_vals_sub) <= D and max(c_vals_sub) - min(c_vals_sub) <= D:
            return True
        
        # Tenta com o ponto de max_d
        candidates = [i for i in range(n) if d_vals[i] >= max_d - D]
        a_vals_sub = [a_vals[i] for i in candidates]
        b_vals_sub = [b_vals[i] for i in candidates]
        c_vals_sub = [c_vals[i] for i in candidates]
        if max(a_vals_sub) - min(a_vals_sub) <= D and max(b_vals_sub) - min(b_vals_sub) <= D and max(c_vals_sub) - min(c_vals_sub) <= D:
            return True
        
        return False
    
    # Busca binária na resposta
    lo = 0
    hi = max(max_a - min_a, max_b - min_b, max_c - min_c, max_d - min_d)
    while lo < hi:
        mid = (lo + hi) // 2
        if can(mid):
            hi = mid
        else:
            lo = mid + 1
    print(lo)

if __name__ == "__main__":
    main()